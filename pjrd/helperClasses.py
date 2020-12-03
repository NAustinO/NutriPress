
import pymysql
import sys
import os
from operator import itemgetter
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from typing import Union
sys.path.append('/pjrd')
sys.path.append('..')


"""
Class Docstring Template
----------------------------

    '''
    Description:
        
    Methods:
        
    Attributes:
         
    '''

Class Method/Function Template 
----------------------------

    '''
    Purpose:
        
    Arguments:
        
    Returns:
        
    '''


"""


class CustomTableModel(QAbstractTableModel):
    def __init__(self, horizHeaders: list = None, tableData=None, vertHeaders: list=None):
        super(CustomTableModel, self).__init__()
        self.tableData = tableData
        self.horizHeaders = horizHeaders
        self.vertHeaders = vertHeaders

    def rowCount(self, parent: QModelIndex):
        if self.tableData is None:
            return 0
        else:
            return len(self.tableData)
    
    def columnCount(self, parent: QModelIndex):
        if self.tableData is None:
            if self.horizHeaders is None:
                return 0
            else:
                return len(self.horizHeaders)
        else:
            return len(self.tableData[0])

    def inputTableData(self, tableData):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.tableData = tableData
        self.emit(SIGNAL("layoutChanged()"))
    
    def setHeaderLabels(self, headerList, orientation, role):
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            self.vertHeaders = headerList
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            self.horizHeaders = headerList
        for index, value in enumerate(headerList):
            self.setHeaderData(index, orientation, value, role=role)
        self.emit(SIGNAL("headerDataChanged()"))

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.tableData[index.row()][index.column()]
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        else:
            return 

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if self.horizHeaders is None:
                return
            return self.horizHeaders[section]
        if role == Qt.DisplayRole and orientation == Qt.Vertical:
            if self.vertHeaders is None:
                return
            return self.vertHeaders[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def sort(self, nCol, order):
        try:
            self.emit(SIGNAL("layoutAboutToBeChanged()"))
            self.tableData = sorted(self.tableData, key=itemgetter(nCol))
            if order == Qt.DescendingOrder:
                self.tableData.reverse()
            self.emit(SIGNAL("layoutChanged()"))
        except Exception:
            return



class UnitOfMeasure(QStandardItem):
    '''

    Description:
        Class to hold unit data
    Methods:
        pass
    Attributes:
        inputWeight - the user inputted weight that is contained within the formula
        conversionFactor - the multiplier to convert to the database consistent unit of measure
        conversionOffset - the number offset to use before multiplying by the conversion factor to get the database-consistent unit of measure
    '''

    def __init__(self, unitID: int, unitName: str, conversionFactor=None, conversionOffset=None, symbol: str=None):
        self.unitID = unitID
        self.unitName = unitName
        self.conversionFactor = conversionFactor
        self.conversionOffset = conversionOffset
        self.symbol = symbol
    

class Ingredient(object):
    '''
    Description:
        Wrapper class to organize and alter data of each a formula ingredient object. The food description and id is required when declaring an object
    Methods:
        setDesc - sets the food descrition
        setFoodID - sets the foodID
        
        
    Attributes:
        __desc: str = food description
        foodID: int = integer id that uniquely identifies the food from food        database. Each ingredient is contained within the food
        inputWeight- a tuple representing the inputted float weight coupled with the unit object
    '''

    def __init__(self, desc: str, foodID: int, inputWeight: Union[float, int] = None, unit: UnitOfMeasure = None, supplierID: int = None, supplierName: str = None, supplierItemCode: str = None, specificName: str = None, ingredientStatement: str = None):
        self.desc = desc
        self.foodID = foodID
        self.inputWeight = inputWeight
        self.unit = unit
        self.supplierName = supplierName
        self.supplierID = supplierID
        self.supplierItemCode = supplierItemCode
        self.specificName = specificName
        self.ingredientStatement = ingredientStatement
        self.__inputWeightInGrams = None
        self.nutrients = {{}} 

    @property
    def inputWeightInGrams(self):
        if self.unit or self.inputWeight is None:
            return False
        elif self.__inputWeightInGrams is not None:
            return self.__inputWeightInGrams
        else:
            self.__inputWeightInGrams = (self.inputWeight + self.unit.conversionOffset) * self.unit.conversionFactor
            return self.__inputWeightInGrams

    # sets attribute
    def setInputWeightInGrams(self, newWeight):
        self.__inputWeightInGrams = newWeight


class Nutrient(object):

    def __init__(self, nutrientID: int, nutrientName: str, dailyValueInGrams: float = None):
        self.nutrientID = nutrientID
        self.nutrientName = nutrientName
        self.dailyValueInGrams = dailyValueInGrams


class Formula(object):

    def __init__(self, formulaName: str, formulaID: int=None, versionNumber = None, isRevision: bool = None, prevRevisionID = None):
        self.formulaName = formulaName
        self.formulaID = formulaID
        self.versionNumber = versionNumber
        self.isRevision = isRevision
        self.prevRevisionID = prevRevisionID
        self.totalWeightG = 0
        self.categories = [] # list of categories that the formula can be attributed to 
        self.allergens = [] # list of all allergens
        self.claims = [] # list of all claims that can be made
        self.__currentIngredients = {{}} # holds the ingredients, maybe map by ingredientID?
        self.servingSize = None
        self.servingWeight = None
        self.numberOfServings = None

        '''
        {
            foodID: {
                'object': Ingredient
                'percentByWeight': float
                ''
            }
        }

        '''
    def currentIngredients(self):
        self.calculateTotalFormulaWeight()
        self.refreshPercentByWeight()
        return self.__currentIngredients
    
    def addIngredient(self, ingredient: Ingredient):
        self.totalWeightG += ingredient.inputWeightInGrams

        # if the ingredient already exists in the formula
        if ingredient.foodID in self.__currentIngredients:
            dict = self.__currentIngredients.get(ingredient.foodID)
            existingIngredient = dict['object']
            newWeight = existingIngredient.inputWeightInGrams + ingredient.inputWeightInGrams
            existingIngredient.setInputWeightInGrams(newWeight)
            #dict['percentByWeight'] = (existingIngredient.inputWeightInGrams/self.totalWeightG) * 100

        # if the ingredient does not already exist in the formula
        else:
            self.__currentIngredients[ingredient.foodID]['object'] = ingredient
            self.__currentIngredients[ingredient.foodID]['percentByWeight'] = (ingredient.inputWeightInGrams/self.totalWeightG) * 100

    def removeIngredient(self, ingredient: Ingredient):
        if ingredient.foodID in self.__currentIngredients:
            ingredientToRemove = self.__currentIngredients[ingredient.foodID]
            self.totalWeightG -= ingredientToRemove.inputWeightInGrams
            self.__currentIngredients.remove(ingredient.foodID)
            self.refreshPercentByWeight()
            return True
        else:
            return False

    def getIngredientPercentWeight(self, ingredient: Ingredient):
        if ingredient.foodID in self.__currentIngredients:
            self.refreshPercentByWeight()
            return self.__currentIngredients[ingredient.foodID]['percentByWeight']
        else:
            return 0

    def refreshPercentByWeight(self):
        for ingredient in self.__currentIngredients:
            ingredient['percentByWeight'] = (ingredient['object'].inputWeightInGrams/self.totalWeightG) * 100

    def calculateTotalFormulaWeight(self):
        self.totalWeightG = 0
        for ingredient in self.__currentIngredients:
            self.totalWeightG += ingredient['object'].inputWeightInGrams
        