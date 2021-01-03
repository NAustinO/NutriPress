
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
from typing import cast


"""
Class Docstring Template
----------------------------

    '''
    Description:
        
    Methods:
        
    Attributes:
         
    '''
"""
#Class Method/Function Template 


"""
----------------------------

    
    Purpose:
        
    Arguments:
        
    Returns:
        

"""

"""
-----------------------------
    Purpose:
    Arguments: 
    Returns:
"""


class CustomTableModel(QAbstractTableModel):
    """
    Class CustomTableModel
    ----------------------------
        '''
        Description: Provides a table model to interact with the QTableView module in QT 
            
        Methods:
        - rowCount: returns the number of rows currently in the table. If no table data is present, returns 0
        - columnCount: returns the number of columns currently in the table. Returns the length of the first row if there is tableData, otherwise returns the length of the horizontalHeader if there is one, else returns 0
        - inputTableData: allows user to input a 2DArray. Sets the tableData attribute to the input 
        - setHeaderLabels: takes in an array of desired header labels and QT defined orientations and roles. Sets horizHeaders or vertHeaders based on orientation, and sets the base class headerData to the array values
        - data: required method for QTableView implementation to display data
        - headerData: required method for QTableView implemenentation to display the headers in table
        - sort: allows basic sorting of the specified column by descending or ascending order
        Attributes:
        - tableData: 2D data table 
        - horizHeaders: horizonal header row data (if any)
        - vertHeaders: vertical header row data (if any)
        '''
    """

    def __init__(self, horizHeaders: list = None, tableData=None, vertHeaders: list=None):
        """
        -----------------------------
            Purpose:
            Arguments: 
            Returns:
        """
        super(CustomTableModel, self).__init__()
        self.tableData = tableData
        self.horizHeaders = horizHeaders
        if horizHeaders is not None:
            self.setHeaderLabels(horizHeaders, Qt.Horizontal)
        self.vertHeaders = vertHeaders
        if vertHeaders is not None:
            self.setHeaderLabels(vertHeaders, Qt.Vertical)

    # returns the number of rows 
    def rowCount(self, parent: QModelIndex):
        """
        -----------------------------
            Purpose: overloaded method for implementation of QTableModel
            Arguments: QModelIndex
            Return Value: 
                -Returns the number of rows in the table. If there is no table data, returns 0
        """
        if self.tableData is None:
            return 0
        else:
            return len(self.tableData)

    # returns the number of columns 
    def columnCount(self, parent: QModelIndex):
        """
        -----------------------------
            Purpose: overloaded method for implementation of QTableModel
            Arguments: QModelIndex
            Return Value:
                - Returns the number of columns in the table.
                - If there is no table data, uses the length of the horizontal headers if the table contains any. Otherwise it returns 0
        """
        if self.tableData is None:
            if self.horizHeaders is None:
                return 0
            else:
                return len(self.horizHeaders)
        else:
            return len(self.tableData[0])

    def inputTableData(self, tableData):
        """
        -----------------------------
            Purpose: Allows user to input a 2d dataframe to the table. Emits a signal to update the viewport for the QTableView that represents the data
            Arguments:
                - tableData: 2D array of data
            Return Value: None
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.tableData = tableData
        self.emit(SIGNAL("layoutChanged()"))
    
    # overwrite of se
    def setHeaderLabels(self, headerList: list, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        """
        -----------------------------
            Purpose: Allows addition of headers that will be displayed in the QTableView that represents this model
            Arguments: 
                - headerList: a list of strings containing the designated headers. The index of the headerList corresponds to the column index of the QTableView
                - orientation: A Qt Namespace designated to indicate whether the headers should display as columns, or as rows
                - role: Indicates to the QTableView how to interpret and display the data
            Return Value: None
        """
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            self.vertHeaders = headerList
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            self.horizHeaders = headerList
        for index, value in enumerate(headerList):
            self.setHeaderData(index, orientation, value, role=role)
        self.emit(SIGNAL("headerDataChanged()"))

    def data(self, index: QModelIndex, role: Qt.ItemDataRole):
        """
        -----------------------------
            Purpose:
                - Overloaded method for QTableView implementation. Indicates how the QTableView should interact with the dataframe
            Arguments: 
                - index: object used to navigate the data in model
                - role: Used by the QTableView to indicate to the model which type of data it needs
            Return Value:
                - varies by role passed in
        """
        if role == Qt.DisplayRole:
            return self.tableData[index.row()][index.column()]
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        else:
            return

    def headerData(self, section, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        """
        -----------------------------
            Purpose:
                -
            Arguments: 
                - section: the index for the header value to return
                - orientation: A Qt Namespace designated to indicate whether the headers should return the vertical or horizontal header
                - role: Used by the QTableView to indicate to the model which type of data it needs
            Return Value:
                - returns the value given in the header list indicated by the section index
        """
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if self.horizHeaders is None:
                return
            return self.horizHeaders[section]
        if role == Qt.DisplayRole and orientation == Qt.Vertical:
            if self.vertHeaders is None:
                return
            return self.vertHeaders[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def sort(self, nCol: int, order: Qt.SortOrder):
        """
        -----------------------------
            Purpose:
                - Overloaded method to allow basic sorting of the QTableView 
                - Only allows sorting based on columns
            Arguments: 
                - nCol: the index for the column to sort by 
                - order: Indicates how the sort order should be. Either Qt.Ascending or Qt.Descending
            Return Value:
                - None
        """
        try:
            self.emit(SIGNAL("layoutAboutToBeChanged()"))
            self.tableData = sorted(self.tableData, key=itemgetter(nCol))
            if order == Qt.DescendingOrder:
                self.tableData.reverse()
            self.emit(SIGNAL("layoutChanged()"))
        except Exception:
            return


class UnitOfMeasure(QStandardItem):

    """
    Class UnitOfMeasure
    ----------------------------

        '''
        Description: Class to hold unit data
        Methods: None
        Attributes:
            - unitID: unique integer identifier for the unit in the database
            - unitName: unit name
            - symbol: unit symbol
            - conversionFactor - the multiplier to convert to the database consistent unit of measure (grams for weight in most cases)
            - conversionOffset - the number offset to use before multiplying by the conversion factor to get the database-consistent unit of measure
        '''
    """

    def __init__(self, unitID: int, unitName: str, conversionFactor=None, conversionOffset=None, symbol: str=None):
        super(UnitOfMeasure, self).__init__()
        self.unitID = unitID
        self.unitName = unitName
        self.conversionFactor = conversionFactor
        self.conversionOffset = conversionOffset
        self.symbol = symbol

    @staticmethod
    def convertToGrams(value: Union[float, int], unitFrom):
        """
        -----------------------------
            Purpose:
                - Static method to convert a given number into a gram equivalent
            Arguments: 
                - value: the weight quantity to be converted 
                - unitFrom: the Unit object the value is currently in 
            Return Value:
                - Returns a float or integer containing that represents the gram value
        """
        factor = unitFrom.conversionFactor
        offset = unitFrom.conversionOffset
        value = (value + offset) * factor
        return value
    
class Nutrient(object):

    """
    Class Nutrient
    ----------------------------
        '''
        Description: Class designed to store unique nutrient amounts and facilitate converting to the commonly measured unit value from a standard gram weight. 
        Designed to be used as unique nutrient objects stored within an ingredient tree for quick reference, update and deletion
            
        Methods:
        - getStdUnitWeightFromG: class method which returns a tuple containing the nutrient amount in its commonly measured weight and its corresponding UnitOfMeasure object 
        - getStdUnitWeight: takes in a numerical gram weight and UnitOfMeasure object that indicates the unit to convert the numerical gram weight to. 
        Returns a tuple with the converted weight and the unit object passed in

        Attributes:
        - nutrientID: unique integer id that identifies the nutrient
        - nutrientName: nutrient name
        - dailyValueInGrams: the converted value for the FDA recommended daily value, converted to a gram weight. Not all nutrients will have a daily value
        - unit: the UnitOfMeasure object which contains the unit the nutrient is typically measured in
        '''
    """

    def __init__(self, nutrientID: int, nutrientName: str, unit: UnitOfMeasure=None, dailyValueInGrams: float = None,): 
        self.nutrientID = nutrientID
        self.nutrientName = nutrientName
        self.dailyValueInGrams = dailyValueInGrams
        self.unit = unit

    def getStdUnitWeightFromG(self, gramWeight):
        """
        -----------------------------
            Purpose:
                - This method converts a numeric value in grams of the nutrient and converts it to the value in the nutrients native unit  
            Arguments: 
                - gramWeight: the weight quantity given in grams of the nutrient to be converted
            Return Value:
                - Returns a tuple containing the converted value and the unit object of the new value
        """
        factor = self.unit.conversionFactor
        offset = self.unit.conversionOffset
        value = gramWeight/factor - offset
        return (value, self.unit)

    @staticmethod
    # returns the inputted gram weight into nutrients typical measuring unit 
    def getStdUnitWeight(gramWeight: Union[float, int], unit: UnitOfMeasure):
        """
        -----------------------------
            Purpose:
                - Similar to getSTdUnitWeightFromG. A static method that takes in the gram weight of the nutrient and converts it to the value specified by the unit object passed in 
            Arguments: 
                - gramWeight: the quantity of a given nutrient to be converted 
                - unit: the unit object to convert to 
            Return Value:
                - Returns  atuple containing the converted value and the unit object passed in 
        """
        factor = unit.conversionFactor
        offset = unit.conversionOffset
        value = gramWeight/factor - offset
        return (value, unit)

class Ingredient(object):

    """
    Class Ingredient
    ----------------------------

        '''
        Description:class to organize, reference and alter data of an ingredient. The food description and id is required when declaring an object. 
        Designed to be used within a formula
            
        Methods:
        - addNutrient: takes in a nutrient object and amount of said nutrient (in grams). If the nutrient already exists in the ingredient, it simply returns. 
        If the nutrient is not in the nutrientDict, then it will add a new key,value pair of nutrientID, and value with the nutrientObject and amount
        - setNutrietntAmountG: takes in a nutrient object and amount of said nutrient (in grams). 
        If the nutrient already exists in the ingredient, it replaces the old amount with the new amount in the nutrient data structure. 
        If the nutrient does not exist in the ingredient, it will add the nutrient similar to as calling addNutrient()
        - getInputtedQuantity: returns the __inputWeightInGrams attribute as a converted value with the nutrient UnitOfMeasure object as a tuple
        - getInputWeightInGrams: returns the attribute of weight in grams contained in the formula
        - setInputWeightInGrams: takes in a numerical value and sets the __inputWeightInGrams attribute to the new value
            
        Attributes:
        - desc: the ingredient description used in the database
        - foodID: unique integer that identifies the food from the food database. Each ingredient is contained within the food
        - unit: UnitOfMeasure object that holds the unit that the user originally specified when inputting into the formula. 
        Can be used to convert back to the user inputted unit when opening back from database
        - supplierName: supplier name (if any)
        - supplierID: stores the supplierID (if any)
        - supplierItemCoe: stores the supplier item code (if any)
        - specific name: stores the specific name (if any)
        - ingredientStatement: stores the ingredient statement (if any)
        - __inputWeightInGrams: stores how much of the ingredient is in the formula in grams 
        - nutrientDict: data structure to quickly reference the nutrients contained within a given amount of the ingredient

        '''
    """

    def __init__(self, desc: str, foodID: int, unit: UnitOfMeasure = None, supplierID: int = None, supplierName: str = None, supplierItemCode: str = None, specificName: str = None, ingredientStatement: str = None):
        self.desc = desc
        self.foodID = foodID
        self.unit = unit  # UnitOfMeasure object for what unit the weight was inputted as 
        self.supplierName = supplierName
        self.supplierID = supplierID
        self.supplierItemCode = supplierItemCode
        self.specificName = specificName
        self.ingredientStatement = ingredientStatement
        self.__inputWeightInGrams = None
        self.nutrientDict = {} # maps the nutrient id to a nutrient object, which contains data to display information
        '''
        ------self.nutrientDict item example--------
        {
            nutrient_id: {
                'object': Nutrient Object
                'amountInIngredientG': amount of the nutrient that is contained within the ingredient measured in grams
            }     
        }
        '''
    
    def addNutrient(self, nutrient: Nutrient, amountInGrams):
        """
        -----------------------------
            Purpose:
                - For the ingredient object, allows a nutrient object to be stored within. Saves the nutrient and its quantity in a dictionary data structure as long as the nutrient does not already exist in the data structure
            Arguments: 
                - nutrient: The nutrient object which contains accessible information from the database, including the nutrient ID, nutrient name, Recommended daily value (if any), and the unit object which encapsulates unit information for how the nutrient is typically measured
                - amountInGrams: The amount of nutrient in grams that is contained within the ingredient
            Return Value:
                - None
        """
        if nutrient.nutrientID in self.nutrientDict:
            print('Nutrient already exists in ingredient')
            return
        else:
            keys = ['object', 'amountInIngredientG']
            self.nutrientDict[nutrient.nutrientID] = dict.fromkeys(keys)
            self.nutrientDict[nutrient.nutrientID]['object'] = nutrient
            self.nutrientDict[nutrient.nutrientID]['amountInIngredientG'] = amountInGrams
    

    def setNutrientAmountG(self, nutrient: Nutrient, amountInGrams: Union[float, int]):
        """
        -----------------------------
            Purpose:
                - Allows modification of the nutrient dictionary data structure. If the nutrient is not in the ingredient object data structure already, it becomes the same as the addNutrient method. If the nutrient does exist, it will update the amount in the ingredient with the new amountInGrams parameter
            Arguments:
                - nutrient: The nutrient object 
            Return Value:
                - None
        """
        if nutrient.nutrientID not in self.nutrientDict:
            keys = ['object', 'amountInIngredientG']
            self.nutrientDict[nutrient.nutrientID] = dict.fromkeys(keys)
            self.nutrientDict[nutrient.nutrientID]['amountInIngredientG'] = amountInGrams
            self.nutrientDict[nutrient.nutrientID]['object'] = nutrient
        else:
            self.nutrientDict[nutrient.nutrientID]['amountInIngredientG'] = amountInGrams

    # returns a tuple of the quantity and unit the user inputted originally
    def getInputtedQuantity(self):
        """
        -----------------------------
            Purpose:
                - The ingredient object stores the user inputs for amount of the ingredient in the formula and the unit. Allows access to this data by returning a tuple contaning the numeric value inputted and the unit object 
            Arguments: 
                - None
            Return Value:
                - Returns a tuple containing the inputs for the numeric value and the unit object
        """
        factor = self.unit.conversionFactor
        offset = self.unit.conversionOffset
        inputWeightInGrams = self.getInputWeightInGrams
        inputtedQuantity = (inputWeightInGrams/factor) - offset
        return (inputtedQuantity, self.unit)

    @property
    def getInputWeightInGrams(self):
        """
        -----------------------------
            Purpose:
                - Allows access to the weight in grams of the ingredient in the formula
            Arguments: 
                - None
            Return Value:
                - Returns the value for the weight in grams of the ingredient in the formula
        """
        return self.__inputWeightInGrams

    # sets attribute
    def setInputWeightInGrams(self, weight: Union[float, int]):
        """
        -----------------------------
            Purpose:
                - Allows modification of the weight in grams of the ingredient in the formula
            Arguments: 
                - weight: the new weight to be set
            Return Value:
                - None
        """
        self.__inputWeightInGrams = weight


class Formula(object):
    

    """
    Class Formula
    ----------------------------

        '''
        Description: The backend data structure to store a formulas ingredients, the ingredients nutritional values and units. 
        A formula object is created during the formulaEditor initialization to store this information
            
        Methods:
        - refreshNutritionals: returns the allNutritionals dictionary that is updated according to its ingredients
        - getNumberOfIngredients: returns the number of ingredients stored in formula
        - getAllNutritionals: returns the allNurtitionals dictionary
        - nutrientExists: takes in either a nutrientID or a nutrient object. 
        Returns a boolean determining if the formula contains the nutrient. 
        - addIngredient: adds an ingredient to the __currentIngredients data structure if not in it already.
        If it does exist, then adds to the amount already existing. Also refreshes the table in the formulaEditor page
        - removeIngredient: removes the ingredient from the __currentIngredients data structure and updates the percentage by weight values in data structure. 
        Updates the table in formulaEditor page. Returns true if successful, otherwise false
        - refreshTablePercentages: refreshes the table weight percentages in the formulaEditor page
        - getIngredientPercentWeight: takes in either an ingredient object or foodID. Returns the percent by weight value in the formula
        - ingredientExists: takes in an ingredient object. Returns a boolean indicating if the ingredient is already in the __currentIngredients data structure
        - setReplacementIngredient: takes in an ingredient object. Assuming ingredient is in the current ingredients, replaces the existing ingredient with the new one
        in the __currentIngredients data structure. Updates the allNutritionals nutrient amounts, refreshes the ingredient percent weights. 
        Updates the formulaEditor table 
        - getNutrientQuantity: takes in a nutrientID. Returns a tuple contaning the amount of nutrient in grams and the native unit in case further conversion is necessary. 
        - addToExistingIngredient: takes in a ingredient object. Adds the object input weight to the existing object input weight. 
        Updates the allNutritionals nutrient amounts, as well as the amount in the ingredient. Refreshes the ingredient percent weights in data structure. 
        Updates the table in formulaEditor page.
        - refreshPercentByWeight: takes in a boolean, default is none. Refreshes the ingredient percent by weights in the __currentIngredients data structure. 
        - setPercentByWeight: takes in a percent value, and either an ingredient object or foodID. Sets the percent by weight value equal to the argument value. 
        - totalFormulaWeight: returns the total weight in grams of the formula as it has been entered by the user
        - isNutrientIn Formula: takes in a nutrient id. Returns a boolean, indicating whether it is in the allNutritionals data structure
            
        Attributes:
        - formulaName: formula name
        - formulaID: unique formula ID. May not be useful since we don't get the formula id until after it is inputted into database. Could be useful for when the formula is reoped. 
        Can add into the formSubmit method if formulaID is not none to preserve integrity
        - versionNumber
        - isRevision
        - __totalWeightG: total formula weight
        - categories 
        - allergens
        - claims
        - servingSize
        - servingWeight
        - numberOfServings
        - formulaTableRef: a reference to the FormulaEditor table that allows the class methods to interact with the table
        - allNutritionals: a data structure that allows reference to the nutrients contained within the formula
        - __currentIngredients: a data structure that stores the ingredients that are within the formula

        '''
    """

    '''
    DATA STRUCTURE
    ----------------------------------

        -----formula attributes-----
        -formulaName: str 
        -formulaID: int
        -versionNumber: int 
        -isRevision: bool
        -prevRevisionID: int
        -totalWeightG: float
        -categories = str[]
        -allergens = str[]
        -claims = str[]
        -servingSize
        -servingWeight
        -numberOfServings

        -----formula ingredient dictionary-----
        currentIngredients = {
            foodID: {
                'percentByWeight': 
                'object': ingredientObject = 

                    -----ingredient attributes------
                    -desc
                    -foodID
                    -inputWeight
                    -unit
                    -supplierName 
                    -supplierID
                    -supplierItemCode
                    -ingredientStatement 
                    -inputWeightInGrams

                    -----ingredient nutrient dictionary------
                    nutrientDict = {

                        nutrientID: {
                            'amountInIngredientG': 

                            'object': nutrientObject = {
                                ---nutrient attributes---
                                -nutrientID
                                -nutrientName
                                -dailyValueInG

                                -unit = unitObject = {
                                    -----unit attributes-----
                                    unitID
                                    unitName
                                    conversionFactor
                                    conversionOffset
                                    symbol
                                }
                            }
                        }
                    }

            },
            ...
        }

        -----formula nutritionals dictionary-----
        allNutritionals = {
            nutrientID: {
                'totalInG': 
                'dailyValueInG': 
                'unit': unitObject = {
                    -----unit attributes-----
                    unitID
                    unitName
                    conversionFactor
                    conversionOffset
                    symbol
                }
            }
        }
    
    '''

    def __init__(self, formulaName: str, formulaID: int=None, versionNumber = None, isRevision: bool = None, prevRevisionID = None, formulaTableRef: QTableWidget = None, mainWindow = None):
        self.formulaName = formulaName
        self.formulaID = formulaID
        self.versionNumber = versionNumber
        self.isRevision = isRevision
        self.prevRevisionID = prevRevisionID
        self.__totalWeightG = 0
        self.categories = [] # list of categories that the formula can be attributed to 
        self.allergens = [] # list of all allergens
        self.claims = [] # list of all claims that can be made
        self.servingSize = None
        self.servingWeight = None
        self.numberOfServings = None
        self.formulaTableRef = formulaTableRef # reference to the table in the formula editor page that needs to be edited 
        self.mainWindow = mainWindow
        self.ingStatement = None
        self.allNutritionals = {}  # {{}}#  stores the totals for each nutritional for faster lookup times 
        ''' 
        ------allNutritionals data structure item example-----
        {
            nutrient_id: {
                'totalInG': 
                'dailyValueInG':
                'unit':
            },
            ...
        }
        '''

        self.__currentIngredients = {} # {{}} # holds the ingredients, maybe map by ingredientID?

        '''
        ------currentIngredients data structure item example-------
        {
            foodID: {
                'object': Ingredient 
                'percentByWeight': the percent by weight of the ingredient in the formula
                
            },
            ....
        }
        '''

    # returns the allNutritionals data structure that has been updated 
    def refreshNutritionals(self):
        """
        -----------------------------
            Purpose: 
                - Ensures that the allNutritionals data structure is updated
                - For each ingredient in the formula, iterates through each nutrient contained in the ingredient and adds its value to the total nutrient content for the formula, as well as applies the daily value and unit object
                - Uses a nested for loop with O(n * m). n = # of ingredients, m ≈ 80 nutrients(max). Called on each addition of a new ingredient to formula
            Arguments: 
                - None
            Return Value:
                - Returns a reference to the newly updated allNutritionals data structure
        """
        keys = ['totalInG', 'unit', 'dailyValueInG']
        temp = {}
        for ingDict in self.__currentIngredients.values():
            ingredientObject = ingDict['object']
            for nutrientID, dictItem in ingredientObject.nutrientDict.items():
                if nutrientID not in temp:
                    
                    nutrientObject = ingredientObject.nutrientDict[nutrientID]['object']
                    tempNutrDict = dict.fromkeys(keys)
                    tempNutrDict['unit'] = nutrientObject.unit
                    tempNutrDict['totalInG'] = dictItem['amountInIngredientG']
                    tempNutrDict['dailyValueInG'] = nutrientObject.dailyValueInGrams
                    temp[nutrientID] = tempNutrDict
                else:
                    temp[nutrientID]['totalInG'] += dictItem['amountInIngredientG']
        self.allNutritionals = temp
        return self.allNutritionals

    def getNumberOfIngredients(self):
        """
        -----------------------------
            Purpose: 
                - Returns the number of ingredients contained within the currentIngredients data structure
            Arguments: 
                - None  
            Return Value:
                - Returns the number of ingredients
        """
        return len(self.__currentIngredients)
        
    
        
    # returns the dictionary containing all the current ingredients with the percentByWeight
    def getCurrentIngredients(self):
        """
        -----------------------------
            Purpose: 
                - Allows access to the currentIngredients dictionary
            Arguments: 
                - None
            Return Value:
                - Returns the currentIngredients dictionary containing all the current ingredients and their percentByWeight values
        """
        self.refreshPercentByWeight()
        return self.__currentIngredients


    # returns the dictinoary containing the nutrient information for the formula
    def getAllNutritionals(self):
        """
        -----------------------------
            Purpose: 
                - Allows access to the allNutritionals dictionary data structure containing the nutrient information for the formula
            Arguments: 
                - None
            Return Value:
                - Returns the reference to the allNutritionals dictionary
        """
        self.refreshNutritionals()
        return self.allNutritionals
        

    # takes in either a nutrientID or a nutrient object. Returns a boolean determining if the formula contains the nutrient by the allNutritionals data structure
    def nutrientExists(self, nutrientID: int = None, nutrient: Nutrient = None):
        """
        -----------------------------
            Purpose: 
                - Determines whether a nutrient exists in the formula.
            Arguments: 2 options to use this method 
                - nutrientID: The id for the nutrient in the database
                - nutrient: The nutrient object
            Return Value:
                - Returns None if no nutrientID or nutrient is given
                - Returns a boolean if the nutrient exists in the formula
        """
        if nutrientID is None and nutrient is None:
            return None
            
        if nutrientID is None:
            if nutrient.nutrientID is None:
                return None
            nutrientID = nutrient.nutrientID
        if nutrientID in self.allNutritionals:
            return True
        else: 
            return False


    # adds an ingredient object to the data structure
    def addIngredient(self, ingredient: Ingredient):
        """
        -----------------------------
            Purpose: 
                - Allows an ingredient to be added to the data structure. 
                - If the ingredient already exists in the formula, adds the amount(stored within the object) to the existing object and refreshes each ingredients % of formula. Calls the addToExistingIngredient method
                - if the ingredient does not currently exist in the formula, adds it to the ingredient data structure
                - Once the ingredient has been created or updated, updates the formula table on the FormulaEditor window. Calls FormulaEditor.refresh() to refresh the different widgets on the FormulaEditor window
            Arguments: 
                - ingredient: the Ingredient object to add
            Return Value:
                - None
        """
        # if the ingredient already exists in the formula
        if ingredient.foodID in self.__currentIngredients:
            self.addToExistingIngredient(ingredient)

        # if the ingredient does not already exist in the formula
        else:
            # sets the ingredient object to the data strcuture
            keys = ['object', 'percentByWeight']
            self.__currentIngredients[ingredient.foodID] = dict.fromkeys(keys)
            self.__currentIngredients[ingredient.foodID]['object'] = ingredient
            for key, value in ingredient.nutrientDict.items():
                if key in self.allNutritionals:
                    if value['amountInIngredientG'] is None:
                        continue
                    self.allNutritionals[key]['totalInG'] += value['amountInIngredientG']
                else:
                    keys = ['totalInG', 'dailyValueInG', 'unit']
                    self.allNutritionals[key] = dict.fromkeys(keys)
                    if value['amountInIngredientG'] is None:
                        self.allNutritionals[key]['totalInG'] = 0
                    else: 
                        self.allNutritionals[key]['totalInG'] = value['amountInIngredientG']
                        self.allNutritionals[key]['dailyValueInG'] = value['object'].dailyValueInGrams
                        self.allNutritionals[key]['unit'] = value['object'].unit
            self.refreshPercentByWeight()
    

        # updates the table 
        if self.formulaTableRef.rowCount() == 0: 
            rowIndex = 0
        else: 
            rowIndex = self.formulaTableRef.rowCount() == 0 


        #ingredient name,% by weight, quantity, unit, supplier, item number,    
        self.formulaTableRef.insertRow(rowIndex)
        nameItem = QTableWidgetItem()
        nameItem.setData(Qt.UserRole, ingredient.foodID)
        nameItem.setText(ingredient.desc.title())
        self.formulaTableRef.setItem(rowIndex, 0, nameItem) # ingredient name 

        percentByWeight = self.getIngredientPercentWeight(ingredient)
        self.formulaTableRef.setItem(rowIndex, 1, QTableWidgetItem(str(percentByWeight))) # ingredient % 

        gramWeight = ingredient.getInputWeightInGrams
        conversionFactor = ingredient.unit.conversionFactor
        conversionOffset = ingredient.unit.conversionOffset
        quantity = gramWeight/conversionFactor - conversionOffset
        
        self.formulaTableRef.setItem(rowIndex, 2, QTableWidgetItem(str(quantity))) # quantity
        self.formulaTableRef.setItem(rowIndex, 3, QTableWidgetItem(ingredient.unit.unitName.lower()))  # unit name
        if ingredient.supplierName is None:
            self.formulaTableRef.setItem(rowIndex, 4, QTableWidgetItem('-'))
        else:
            self.formulaTableRef.setItem(rowIndex, 4, QTableWidgetItem(ingredient.supplierName)) # supplier

        if ingredient.supplierItemCode is None:
            self.formulaTableRef.setItem(rowIndex, 5, QTableWidgetItem('-'))
        else:
            self.formulaTableRef.setItem(rowIndex, 5, QTableWidgetItem(ingredient.supplierItemCode)) # supplier item number
        
        self.formulaTableRef.update()
        self.mainWindow.refresh()
        self.refreshTablePercentages()
    

    # returns true if succesfully removed ingredient from data structure else false
    def removeIngredient(self, ingredient: Ingredient=None, foodID:int=None):
        """
        -----------------------------
            Purpose: 
                - Removes the ingredient from the data structure. 
            Arguments: 
                - 
            Return Value:
                - Returns True if successfully deleted. Otherwise returns False
        """
        # Error Handling
        # if neither ingredient nor foodID is inputted
        if ingredient is None and foodID is None: 
            print('No ingredient specified in formula.removeIngredient()')
            return False
        # if both ingredient and foodID are inputted but don't match on ID number
        if ingredient is not None and foodID is not None:
            if ingredient.foodID != foodID:
                print('Inconsistent ingredient to remove in formula.removeIngredient(). Ingredient does not match id to remove')
                return False
        
        # assigns ingredient and ID variabels if no errors so far
        if ingredient is None and foodID is not None:
            ingredient = self.__currentIngredients[foodID]['object']
            foodID = ingredient.foodID

        # Error Handling
        if foodID not in self.__currentIngredients:
            print('Ingredient not in currentIngredients for formula.removeIngredient()')
            return False
        else:
            # deducts the ingredient nutrients from the formula nutrient totals
            for key, value in ingredient.nutrientDict:
                self.allNutritionals[key]['totalInG'] -= value['amountInIngredientG']
            self.__currentIngredients.remove(ingredient.foodID) # removes from data structure
            self.refreshPercentByWeight() # refreshes the percent weights ingredient data structure

            # updates the FormulaEditor formula table widget 
            for row in range(self.formulaTableRef.rowCount()):
                self.formulaTableRef.setItem(row, 1, QTableWidgetItem(self.__currentIngredients[foodID]['percentByWeight']))
                if self.formulaTableRef.item(row, 0).data(Qt.UserRole) == foodID:
                    self.formulaTableRef.removeRow(row)
                    self.formulaTableRef.update()
            self.refreshTablePercentages()
            return True

    def refreshTablePercentages(self):
        """
        -----------------------------
            Purpose: 
                - Refreshes the FormulaEditor table widget '% of formula' column only. 
                - This method is called usually upon adding or removing an ingredient, where the % of formula would change for all the ingredients 
                - IMPORTANT: To ensure accurate information, this method should be called following refreshPercentByWeight method. It is not called within this method to allow for flexibility 
            Arguments: 
                - None
            Return Value:
                - None
        """
        for row in range(self.formulaTableRef.rowCount()):
            id = self.formulaTableRef.item(row, 0).data(Qt.UserRole) # id of the ingredient in the table
            percentWeight = self.getIngredientPercentWeight(foodID=id)
            self.formulaTableRef.setItem(row, 1, QTableWidgetItem(str(round(percentWeight, 3))))

    
    # gets the percent by weight in the formula given the ingredient object or ingredient id \\

    def getIngredientPercentWeight(self, ingredient: Ingredient = None, foodID: int=None):
        """
        -----------------------------
            Purpose: 
                - Allows access of what percent of the formula is a certain ingredient given either the Ingredient object or the foodID from the dtabase
                - The ingredient object passed in is only used for its foodID attribute. The ingredient is mapped by reference, only foodID
            Arguments: 
                - ingredient: The ingreident object to find percent by weight
                - foodID: the ingredient ID to find percent by weight
            Return Value:
                - Returns the percent of formula value if ingredient is in formula
                - Returns 0 if the ingredient is not in formula
                - Returns False if there was an error in the parameters passed
        """
        self.refreshPercentByWeight()
        # Error Handling
        if ingredient is None and foodID is None:
            print('Parameter error in formula.getIngredietnPercentWeight()')
            return False
        elif ingredient is not None and foodID is not None:
            if ingredient.foodID != foodID:
                print('')
                return False
        # /Error Handling
        else:
            if foodID is None:
                foodID = ingredient.foodID
            if foodID not in self.__currentIngredients:
                return 0
            else:
                return self.__currentIngredients[foodID]['percentByWeight']

    def ingredientExists(self, ingredient: Ingredient):
        """
        -----------------------------
            Purpose: 
                - Allows determination on whether the ingredient is in the formula
            Arguments: 
                - ingredient: Ingredient object to look for, based on the foodID attribute
            Return Value:
                - Returns True if the ingredient foodID attribute is in the data structure 
                - NOTE: Even if the ingredientObject has a inputWeightInGrams attribute of 0, it will still return true. 
                - Returns False if it is not in the data structure
        """
        if ingredient.foodID in self.__currentIngredients:
            return True
        return False

    def setReplacementIngredient(self, ingredient: Ingredient):
        """
        -----------------------------
            Purpose: 
                - Allows modification of the ingredient data structure by passing in a replacement ingredient, which replaces the ingredient with the same foodID attribute value 
            Arguments: 
                - ingredient: The ingredient object to replace
            Return Value:
                - Returns True if successfully replaces ingredient in data structure
                - Returns False if not successful
        """
        if not ingredient.foodID:
            return False

        if ingredient.foodID not in self.__currentIngredients:
            print('The ingredient is not the current ingredient to replace')
            return False
        
        else:
            try: 
                # updates the formula nutrient totals with the replacement ingredient nutrients
                for key, value in ingredient.nutrientDict.items():
                    difference = self.allNutritionals[key]['totalInG'] - value
                    ['amountInIngredientG']
                    # NOTE: what to do if key(nutrientID) is not a nutrient in formula nutrients

                    # if difference is negative (the replacing ingredient is more than the current)
                    if difference < 0:
                        self.allNutritionals[key]['totalInG'] += difference
                    # if difference is positive (the current ingredient amount is more than the replacing ingredient)
                    elif difference > 0: 
                        self.allNutritionals[key]['totalInG'] -= difference 
                    
                self.__currentIngredients[ingredient.foodID]['object'] = ingredient
                self.refreshPercentByWeight()

                # updates the table
                for row in range(self.formulaTableRef.rowCount()):
                    id = self.formulaTableRef.item(row, 0).data(Qt.UserRole) # id of the ingredient in the table
                    percentWeight = self.getIngredientPercentWeight(foodID = id)
                    self.formulaTableRef.setItem(row, 1, QTableWidgetItem(str(round(percentWeight, 3))))  
                    #self.formulaTableRef.setItem(row, 1, QTableWidgetItem(self.__currentIngredients[id]['percentByWeight']))    
                    if id == ingredient.foodID:  # if the ingredient in the table is the same as the ingredient replacing
                        #self.formulaTableRef.setItem(row, 1, QTableWidgetItem(self.__currentIngredients[id]['percentByWeight']))  # inputs the new percentage by weight
                        quantityUnit = ingredient.getInputtedQuantity()
                        self.formulaTableRef.setItem(row, 2, QTableWidgetItem(str(quantityUnit[0]))) # quantity in origianl unit
                        self.formulaTableRef.setItem(row, 3 , QTableWidgetItem(quantityUnit[1].unitName))
            except Exception:
                return False
            else:
                return True
            
    # returns the nutrient amount in g, along with its native unit 
    def getNutritientQuantity(self, nutrientID: int):
        """
        -----------------------------
            Purpose: 
                - Allows reference to the total nutrient quantity contained in the formula
            Arguments: 
                - nutrientID: the ID number for the nutrient to return
            Return Value:
                - Returns a tuple containing the nutrient amount (in grams) along with its native unit object to allow for conversion if needed
                - Returns False if error
        """
        try:
            quantity = self.allNutritionals[nutrientID]['totalInG']
            unit = cast(UnitOfMeasure, self.allNutritionals[nutrientID]['unit'])
            if not quantity or not unit:
                return False
            
        except Exception:
            print('something went wrong in formula.getNutrientQuantity()')
            return False
        else:
            return (quantity, unit)
            

    # adds weight to an ingredient that exists in the formula already
    def addToExistingIngredient(self, ingredient: Ingredient):
        """
        -----------------------------
            Purpose: 
                - Allows reference to the total nutrient quantity contained in the formula
            Arguments: 
                - nutrientID: the ID number for the nutrient to return
            Return Value:
                - Returns a tuple containing the nutrient amount (in grams) along with its native unit object to allow for conversion if needed
                - Returns False if error
        """

        if ingredient.foodID not in self.__currentIngredients:
            print('The ingredient is not an existing ingredient to be added to')
        else:
            # get temporary current ingredient object
            current = cast(Ingredient, self.__currentIngredients.get(ingredient.foodID)['object']) 

            # add the weights of the current and new ingredient to temporary ingredient object
            current.setInputWeightInGrams(current.getInputWeightInGrams + ingredient.getInputWeightInGrams)
            
            # iterates through nutrient dictionary and updates the allNutritionals data structure
            for nutrientID, idDict in current.nutrientDict.items():
                
                try:
                    self.allNutritionals[nutrientID]['totalInG'] += ingredient.nutrientDict[nutrientID]['amountInIngredientG']


                    # adds the nutrient quantities of the current and new ingredient and stores in temporary ingredient object nutrientDict
                    current.nutrientDict[nutrientID]['amountInIngredientG'] += ingredient.nutrientDict[nutrientID]['amountInIngredientG']

                    # updates the nutrient total for the entire ingredient DONT THINK I NEED THIS
                    #current.nutrientTotalsG[nutrientID] += current.nutrientDict[nutrientID]['amountInIngredientG']
                except:
                    print('Something went wrong adding a nutrient of the current ingredient with the new ingredient in formula.addToExistingIngredient() for nutrient ID %s'.format(nutrientID))
                    pass

            # updates the formula dictionary with the ingredient object
            self.__currentIngredients[ingredient.foodID]['object'] = current

        self.refreshPercentByWeight()

        # updates the table
        for row in range(self.formulaTableRef.rowCount()):
            id = self.formulaTableRef.item(row, 0).data(Qt.UserRole) # id of the ingredient in the table
            percentWeight = self.getIngredientPercentWeight(foodID = id)
            self.formulaTableRef.setItem(row, 1, QTableWidgetItem(str(percentWeight)))    
            if id == ingredient.foodID:  # if the ingredient in the table is the same as the ingredient replacing
                #self.formulaTableRef.setItem(row, 1, QTableWidgetItem(self.__currentIngredients[id]['percentByWeight']))  # inputs the new percentage by weight
                quantityUnit = ingredient.getInputtedQuantity()
                self.formulaTableRef.setItem(row, 2, QTableWidgetItem(str(quantityUnit[0]))) # quantity in origianl unit
                self.formulaTableRef.setItem(row, 3 , QTableWidgetItem(quantityUnit[1].unitName))

    def refreshPercentByWeight(self, refreshTable: bool = None):
        """
        -----------------------------
            Purpose: 
                - Called to update the ingredient data structure so that each ingredient item has the correct percentage
            Arguments: 
                - refreshTable: A boolean argument. If the boolean is true, will also refresh the FormulaEditor formula table #TODO
            Return Value:
                - Returns True if successful, otherwise False
        """
    
        totalFormulaWeight = self.totalFormulaWeight()
        
        # refreshes data in self contained data structure
        for ingredient in self.__currentIngredients.values():
            percent = (ingredient['object'].getInputWeightInGrams/totalFormulaWeight) * 100
            id = ingredient['object'].foodID
            self.setPercentByWeight(percent, foodID=id) 
        return True
        # refreshes data in the the table TODO

    #  takes in a percent value, and either an ingredient object or foodID. Sets the percent by weight value equal to the argument value. 
    def setPercentByWeight(self, percent, ingredient: Ingredient = None, foodID: int = None):
        """
        -----------------------------
            Purpose: 
                - Designed to be a private method 
                - Alters the ingredient data structure to set the percent weight to a new value, given as percent
            Arguments: 
                - percent: The new percent value to replace
                - ingredient: An ingredient object to change. Uses the foodID attribute 
                - foodID:: An ID to identify the ingredient to change
            Return Value:
                - 
        """
        if ingredient and foodID is None:
            print('No ingredient or foodID inputted in formulalsetPercentByWeight()')
            return False
        try:
            if foodID is None:
                foodID = ingredient.foodID
            self.__currentIngredients[foodID]['percentByWeight'] = percent
        except:
            return False
        else:
            return True

    def totalFormulaWeight(self):
        """
        -----------------------------
            Purpose: 
                - To get the total weight of the formula
            Arguments: 
                - None
            Return Value:
                - Returns the sum (in grams) of the ingredients in the formula
        """
        self.__totalWeightG = 0
        for ingredient in self.__currentIngredients.values():
            self.__totalWeightG += ingredient['object'].getInputWeightInGrams
        return self.__totalWeightG
    
    # checks whether the inptuted nutrientID is in the d

    def isNutrientInFormula(self, nutrientID: int):
        """
        -----------------------------
            Purpose: 
                - To check whether a given nutrient is in the formula
                - Realistically, checks whether any of the ingredients in the formula had an input for the nutrient, even 0 
            Arguments: 
                - nutrientID: the ID of the nutrient to check for
            Return Value:
                - Returns a boolean indicating whether the nutrientID has a key in the nutrients data structure
        """
        if nutrientID in self.allNutritionals:
            return True
        return False


