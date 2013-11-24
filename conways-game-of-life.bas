      REM Conway's Game of Life
      INPUT mode%
      IF mode% = 1 THEN
        REM Queen Bee Shuttle
        
        W% = 22
        H% = 9
        
        DIM grid(W%,H%)
        
        grid(2,5) = 1
        grid(2,6) = 1
        grid(3,5) = 1
        grid(3,6) = 1
        
        grid(21,5) = 1
        grid(21,6) = 1
        grid(20,5) = 1
        grid(20,6) = 1
        
        grid(7,5) = 1
        grid(8,4) = 1
        grid(8,6) = 1
        grid(9,3) = 1
        grid(9,7) = 1
        grid(10,4) = 1
        grid(10,5) = 1
        grid(10,6) = 1
        grid(11,3) = 1
        grid(11,2) = 1
        grid(11,7) = 1
        grid(11,8) = 1
        
      ENDIF
      IF mode% = 2 THEN
        REM Init Lightweight Spaceship
        
        W% = 20
        H% = 10
        
        DIM grid(W%,H%)
        
        grid(19,2) = 1
        grid(19,4) = 1
        grid(18,5) = 1
        grid(17,5) = 1
        grid(16,5) = 1
        grid(16,2) = 1
        grid(15,3) = 1
        grid(15,4) = 1
        grid(15,5) = 1
        
      ENDIF
      IF mode% = 3 THEN
        REM Create Block
        
        W% = 10
        H% = 10
        
        DIM grid(W%, H%)
        
        grid(4,5) = 1
        grid(4,6) = 1
        grid(5,5) = 1
        grid(5,6) = 1
      ENDIF
      IF mode% = 4 THEN
        REM Create Hive
        
        W% = 10
        H% = 10
        
        DIM grid(W%, H%)
        
        grid(4,5) = 1
        grid(4,7) = 1
        grid(5,5) = 1
        grid(5,7) = 1
        grid(3,6) = 1
        grid(6,6) = 1
      ENDIF
      
      CLS
      
      REM Time in Seconds...
      TIMEPERIOD = 0.2
      
      PROC_printGrid(grid)
      WAIT TIMEPERIOD*100
      
      WHILE 1
        PROC_updateGrid(grid)
        CLS
        PROC_printGrid(grid)
        WAIT TIMEPERIOD*100
      ENDWHILE
      
      END
      
      REM Procedure definitions
      DEFPROC_updateGrid(RETURN grid)
      LOCAL newgrid()
      DIM newgrid(W%,H%)
      newgrid() = grid()
      
      FOR x%=1 TO W%
        FOR y%=1 TO H%
          num_neighbours = 0
          
          FOR nx%=x%-1 TO x%+1
            FOR ny%=y%-1 TO y%+1
              IF (nx% <> x% OR ny% <> y%) AND (nx% > 0 AND nx% < W%+1 AND ny% > 0 AND ny% < H%+1) THEN
                IF grid(nx%, ny%) = 1 THEN
                  num_neighbours += 1
                ENDIF
              ENDIF
            NEXT ny%
          NEXT nx%
          
          IF grid(x%, y%) = 0 THEN
            IF num_neighbours = 3 THEN
              newgrid(x%, y%) = 1
            ENDIF
          ELSE
            IF num_neighbours < 2 OR num_neighbours > 3 THEN
              newgrid(x%, y%) = 0
            ENDIF
          ENDIF
        NEXT y%
      NEXT x%
      
      grid() = newgrid()
      ENDPROC
      
      DEFPROC_printGrid(grid)
      
      FOR y%=1 TO H%
        FOR x%=1 TO W%
          IF grid(x%, y%) == 1 THEN
            PRINT "+";
          ELSE
            PRINT "_";
          ENDIF
        NEXT x%
        PRINT
      NEXT y%
      PRINT
      
      ENDPROC
