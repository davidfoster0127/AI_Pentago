"""
Author: David Foster
Date: 11/12/2017
"""

import random
from copy import deepcopy
import pentago

# Depth limit of search tree
maxDepth = 2

# Search method to use, 'AlphaBeta' or 'MiniMax'
searchMethod = 'MiniMax'

#Game node class used to create tree
class gameNode:
    state = None
    depth = 0
    value = 0
    prevMove = []
    childNodes = []
    
    #get list of child nodes from the current game state
    def getchildNodes(self, color):
        #get list of possible moves
        moves = self.state.getPossibleMoves()
        
        #create a childnode for each move and add it to the list of childnodes
        for move in moves:
            child = gameNode()
            child.state = pentago.game()
            child.state.board = deepcopy(self.state.board)
            child.state.placePiece(color, move[0], move[1])
            child.state.rotate(move[2], move[3])
            child.prevMove = move
            child.depth = self.depth + 1
            child.childNodes = []
            
            #check for duplicate board states
            nodeExists = False
            for existingNode in self.childNodes:
                if child.state == existingNode.state:
                    nodeExists = True
                    break
                
            #add the new state if it does not exist
            if not nodeExists:
                self.childNodes.append(child)
                
#AI agent class containing MiniMax and AlphaBeta search algorithms
class agent:
    gameTreeRoot = None
    currentNode = None
    maxcolor = ''
    mincolor = ''
    depthLimit = -1

    nExpanded = 0
    
    #get an intelligent move using game tree search
    def getMove(self, current):
        #create the treeroot node or update current node if it already exists
        if self.gameTreeRoot == None:
            self.gameTreeRoot = gameNode()
            self.gameTreeRoot.state = current
            self.gameTreeRoot.depth = 0
            self.gameTreeRoot.prevMove = []
            self.currentNode = self.gameTreeRoot
        else:
            for child in self.currentNode.childNodes:
                if child.state == current:
                    self.currentNode = child
                    break
                
        self.depthLimit = self.currentNode.depth + maxDepth
        
        #find the optimal state
        if searchMethod == 'AlphaBeta':
            nextNode = self.alphaBetaSearch(self.currentNode)
        else:
            nextNode = self.miniMaxSearch(self.currentNode)
        
        print(self.nExpanded)
        self.nExpanded = 0

        #update current node to the optimal state and return the move used to get there
        self.currentNode = nextNode
        return nextNode.prevMove
    
    #MinMax search algorithm functions
    def miniMaxSearch(self, node):
        #get child nodes if none exist
        if(len(node.childNodes) == 0):
            node.getchildNodes(self.maxcolor)
            self.nExpanded += 1
        
        #calculate maximum value
        bestValue = self.MM_maximize(node)
        bestChild = node.childNodes[0]
        
        #find the child with optimal value and return it
        for child in node.childNodes:
            if child.value == bestValue:
                bestChild = child
                break
        return bestChild
    
    def MM_maximize(self, node):
        #check depth to depth limit and return utility if its a terminal node
        if node.depth < self.depthLimit:
            if len(node.childNodes) == 0:
                node.getchildNodes(self.maxcolor)
                self.nExpanded += 1
        if len(node.childNodes) == 0:
            return node.state.getUtility(node.state.getLines(), self.maxcolor, self.mincolor)
        
        #otherwise find max value child    
        maxValue = -float('inf')
        for child in node.childNodes:
            #find minimum of next depth level
            child.value = self.MM_minimize(child)
            maxValue = max(maxValue, child.value)
        return maxValue
    
    def MM_minimize(self, node):
        #check depth to depth limit and return utility if its a terminal node
        if node.depth < self.depthLimit:
            if len(node.childNodes) == 0:
                node.getchildNodes(self.mincolor)
                self.nExpanded += 1
        if len(node.childNodes) == 0:
            return node.state.getUtility(node.state.getLines(), self.maxcolor, self.mincolor)
        
        #otherwise find the minimum value child   
        minValue = float('inf')
        for child in node.childNodes:
            #find maximum of next depth level
            child.value = self.MM_maximize(child)
            minValue = min(minValue, child.value)
        return minValue
        
    #AlphaBeta search algorithm functions
    def alphaBetaSearch(self, node):
        #get child nodes if none exist
        if(len(node.childNodes) == 0):
            node.getchildNodes(self.maxcolor)
            self.nExpanded += 1
        beta = float('inf')
        alpha = -float('inf')
        bestChild = node.childNodes[0]
        
        #get max value child
        for child in node.childNodes:
            #determine value by minimizing next depth level
            child.value = self.AB_minimize(child, alpha, beta)
            if child.value > alpha:
                alpha = child.value
                bestChild = child

        return bestChild

    def AB_maximize(self, node, alpha, beta):
        #check depth to depth limit and return utility if its a terminal node
        if node.depth < self.depthLimit:
            if len(node.childNodes) == 0:
                node.getchildNodes(self.maxcolor) 
                self.nExpanded += 1
        if len(node.childNodes) == 0:
            return node.state.getUtility(node.state.getLines(), self.maxcolor, self.mincolor)
        
        #otherwise find max value child
        value = -float('inf')
        for child in node.childNodes:
            #determine value by minimizing next depth level
            child.value = self.AB_minimize(child, alpha, beta)
            value = max(value, child.value)
            #prune if value is greater or equal to beta by returning current node value
            if value >= beta:
                return value
            alpha = max(alpha, value) 
        return value
        
    def AB_minimize(self, node, alpha, beta):
        #check depth to depth limit and return utility if its a terminal node
        if node.depth < self.depthLimit:
            if len(node.childNodes) == 0:
                node.getchildNodes(self.mincolor)
                self.nExpanded += 1
        if len(node.childNodes) == 0:
            return node.state.getUtility(node.state.getLines(), self.maxcolor, self.mincolor)
        
        #otherwise find min value child
        value = float('inf')
        for child in node.childNodes:
            #determine value by maximizing next depth level
            child.value = self.AB_maximize(child, alpha, beta)
            value = min(value, child.value)
            #prune if value is less or equal to alpha by returning current node value
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value