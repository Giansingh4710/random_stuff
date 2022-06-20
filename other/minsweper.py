
'''
  Let's play minesweeper.
  http://minesweeperonline.com/
  https://en.wikipedia.org/wiki/Minesweeper_(video_game)
  
  Generate a board. Write a function, given a board's dimension(rowNum, colNum), and number of mines(mineNum). 
  Randomly generate a board. 
  Note: rowNum may not equal to colNum.
  
  Example:
  Input: rowNum = 3, colNum = 3, mineNum = 2
  
  One possible output: 0 represents blank, -1 represents a mine. 
  [
    [0, 0, 0], 
    [-1, 0, 0], 
    [0, -1, 0]
  ]
'''
import random

def board(rowNum,colNum,mineNum):
    if mineNum>rowNum*colNum or mineNum<0:
        theBoard=[-1]*rowNum*colNum
    else:
        theBoard=[0 for i in range(colNum*rowNum)]
        mines=set()
        while len(mines)!=mineNum:
            num=random.randint(0,rowNum*colNum-1)
            mines.add(num)            
        for i in mines:
            theBoard[i]=-1
    theBoard=[theBoard[i:i+rowNum] for i in range(0,len(theBoard),rowNum)]
    for i in theBoard:
        print(i)
    return theBoard

board(3,3,-3)
'''

import java.util.*;
public class minsweper{
    public static void main(String[] args){
        int[][] theBoard=board(5,3,90);
        System.out.println("----------------");
        for(int i=0;i<theBoard.length;i++){
            for(int j=0;j<theBoard[i].length;j++){
                System.out.print(theBoard[i][j]+"|");
            }
            System.out.println();
        }
    }
    public static int[][] board(int row,int col,int mines){
        int[] theBoard= new int[row*col];
        if(mines>=row*col){
            for(int i=0;i<row*col;i++){
                theBoard[i]=-1;
            }
        }
        else{
            int minesCount=0;
            while(minesCount<mines){
                double gen=Math.random();
                double gentimes=gen*col*row;
                int rand=(int)(gentimes);
                if(theBoard[rand]==0){
                    theBoard[rand]=-1;
                    minesCount++;
                }
                //System.out.println(rand);
            }
        }
        
        int[][] lstOfLstBoard=new int[row][col];
        int count=0;
        for(int i=0;i<col*row;i+=row){
            int end=i+row;
            int[] newArray=Arrays.copyOfRange(theBoard, i, end);
            lstOfLstBoard[count]=newArray;
            count++;
        }
        
       return lstOfLstBoard; 
       //return theBoard;
    }}

/*
const generateMinesweeperBoard = (rows, cols, numMines) => {

    const totalSquares = rows * cols;



    if (numMines > totalSquares) {

                    throw new Error(`

Number of mines cannot be greater than the number of squares!

Num squares (rows * cols): ${totalSquares}

Num mines: ${numMines}

`);

    }



    const board = [];

    const mineCoordinates = generateMineCoordinates(rows, cols, numMines);



    for (let x = 0; x < rows; x++) {

                    board[x] = [];



                    for (let y = 0; y < cols; y++) {

                                    const key = getMineCoordinatesKey(x, y);



                                    board[x][y] = mineCoordinates.has(key) ? -1 : 0;

                    }

    }



    return board;

};



const generateMineCoordinates = (rows, cols, numMines) => {

    const mineCoordinates = new Set();



    while (mineCoordinates.size < numMines) {

                    const randomRow = getRandomInt(0, rows);

                    const randomCol = getRandomInt(0, cols);

                    const key = getMineCoordinatesKey(randomRow, randomCol);



                    mineCoordinates.add(key);

    }



    return mineCoordinates;

};



const getMineCoordinatesKey = (row, col) => `${row}-${col}`;



const getRandomInt = (min, max) =>

    Math.floor(Math.random() * (max - min)) + min;      
            
        
let a=generateMinesweeperBoard(5,30,10)

for(let i=0;i<a.length;i++){
    console.log(a[i])
}
'''