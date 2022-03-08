#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

// major variables
int range; 
int points=0; 
int xcoordinate=0; 
int ycoordinate=0;
bool win=false;  
bool lose=false;

// functions
int printBoard();
void randomfood();
int startgame();
void randomblocks();
int checkifwin();
int playerstatus();
void moves();
void instruction();
void cleartable();
void addpoint();
int interrorhandler(int min, int max);
void update();


char table[][10][10]={
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"},
    {"[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"}
};

int main(){

  int choice;
  printf("\nGhostless Pac-man \n");
  printf("(1) Start game \n");
  printf("(2) Instructions \n");
  printf("(3) Exit \n\n");
  
  choice=interrorhandler(1,3);
  while (true) 
  {
    switch(choice)
    {
      case 1:
      startgame();

      int choice2;
      printf("\nDo you want to start again\n");
      printf("(1) Yes\n");
      printf("(2) No\n");
      
      choice2=interrorhandler(1,2);

      switch(choice2){
        case 1:
          win=false;
          lose=false;
          cleartable();
          range=0;
          xcoordinate=0;
          ycoordinate=0;
          points=0;

          main();
          break;

        case 2:
          printf("You will now exit the game\n");
          printf("Thank you for playing !\n");
          break;
      }break;


      case 2:
      instruction();

      int choice3;
      printf("\nPress '1' to go back\n");
      choice3=interrorhandler(1,1);

      switch(choice3){
        case 1:
        main();
        break;
      }
      break; 

      case 3: 
      printf("You will now exit the game\n");
      printf("Thank you for playing !\n");
      break;
    }
    break;
  }
  return 0;
}

int startgame(){
  srand(time(NULL));
  randomfood();
  randomblocks();
  moves();

  return 0;
}

void randomfood(){
  int a, b;
  printf("\nNumber of food to be distributed on the board (range 2-9): \n");

  range=interrorhandler(2,9);

  for(int i=0; i<range; i++) {
    
    a=rand() % 10;
    b=rand() % 10;

    if (table[a][b][1] =='*'||(a==0 && b==0) ||(a==6 && b==9)){
      i--;
      continue;
    }
    else{
      table[a][b][1] ='*';
    }
  }
}

void randomblocks(){
  int a, b, c;
  c=(rand() % 10)+2;

  for(int i=0; i<c; i++) {
    
    a=rand() % 10;
    b= rand() % 10;\

    if (table[a][b][1] =='X' || table[a][b][1] =='*' || (a==0 && b==0) ||(a==6 && b==9) ){
      i--;
      continue;
    }
    else{
      table[a][b][1] ='X';
    }
  }
}

void moves(){
  //for printing the aray
  table[xcoordinate][ycoordinate][1] ='o';
  table[6][9][1]='$';

  while (win==false && lose==false){
    int x=xcoordinate;
    int y=ycoordinate;

   //print table
    printf("\n");//dagdag space
    for (int i=0; i<10; i++){
      for (int j=0; j<10; j++){
        printf("%s",table[i][j]);}
      
      printf("\n");
    }

    printf("\n(a): left\n");
    printf("(s): down\n");
    printf("(d): right\n");
    printf("(w): up\n");

     //input moves
    char move[10];

    printf("\nmoves: \n");
    scanf("%s",move);

     //update of the table
    for( int i=0; move[i]!='\0'; i++){  
      
      switch(toupper(move[i])){
        case 'S':
        xcoordinate+=1; 
        addpoint();
        table[x][y][1]=' ';
        x+=1;
        update();


        continue;
       
        case 'W':
        xcoordinate-=1;
        addpoint();
        table[x][y][1]=' ';
        x-=1;
        update();

        continue;
        
        case 'D':
        ycoordinate+=1;
        addpoint();
        table[x][y][1]=' ';
        y+=1;
        update();
        continue;
        
        case 'A':
        ycoordinate-=1;
        addpoint();
        table[x][y][1]=' ';
        y-=1;
        update();
        continue;
        default:
        printf("Your input is undefined\n");
        printf("You can only input the letters 'a', 's', 'w' and 'd' \n");
      
      }
    } 

    printf("\nPoint : %d\n", points);

    table[xcoordinate][ycoordinate][1] ='o';
    
  }
}

int checkifwin(){
  if (xcoordinate<0 || 
  ycoordinate<0 ||
  xcoordinate>9 ||
   ycoordinate>9){
      return 0;}
  else {
    if (table[xcoordinate][ycoordinate][1]=='X'){
    return -1;
  }
    else{
      return 1;
    }
  }
  return 1;
}

int playerstatus(){
  if (points==range && (xcoordinate==6 && ycoordinate==9)){
    win=true;
    return 1;
  }
  else{
    if(points!=range && (xcoordinate==6 && ycoordinate==9)){
      return -2;
    }
    return 0;
  }

  return 0;
}

void addpoint(){
  if (table[xcoordinate][ycoordinate][1]=='*'){
    points+=1;
  }
}

void cleartable(){
  for (int i=0; i<10; i++){
    for ( int j=0; j<10; j++){
      table[i][j][1]=' ';
    }
  }
}

void instruction(){
  printf("Instructions \n");
  printf("Navigation:\n");
  printf("To control Pac-man, the characters W,S,A and D are used. W is used to make it move UP, S to move DOWN, A to go LEFT and D to move RIGHT. When Pac-man collides with any part of the blocks (indicated by X) or any of the boundaries, the game ends and the user loses.\n\n");
  
  printf("Collecting the Food:\n");
  printf("There will be randomly distributed food across the board indicated by *. Points will be accumulated as Pac-man collects the food. Displaying the points will be at the end of the game.\n\n");

  printf("Board Exit:\n");
  printf("When Pac-man eats all the food and moves out of the board. There will be a $ mark on the board indicating the exit point. Once it steps on the marked exit, the game is done and the player wins.\n\n");
}

int interrorhandler(int min, int max){
  while(true){
    int choice;

    printf("Enter a number: \n");
    scanf("%d", &choice);

    if (choice<min || choice>max){
      if (min==max){
        printf("Your input is undefined\n");
        printf("You can only input %d\n", min);
        continue;
      }

      printf("Your input is undefined\n");
      printf("You can only input %d-%d\n", min, max);
      continue;

    }
    else{
      return choice;
    }
  }
}

void update(){
  while(true){
    if (checkifwin()==0){
      printf("Out of boundary. You lose :(((");
      lose=true;
      break;}
    else{
      if(checkifwin()==-1){
        printf("You hit a block. You lose :((");
        lose=true;
        break;
      }}

    if (playerstatus()==1){
      printf("You win !!");
      break;
    }
    else{
      if(playerstatus()==-2){
        printf("You lose, you should have collected all the foods first");
        lose=true;
        break;
      }
    }
    break;
  }
}
