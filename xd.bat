@echo off

REM Run python script in current directory & capture its output in a variable
SET /a COUNT=0
FOR /F "tokens=* USEBACKQ" %%F IN (`python "%~dp0\xd.py" %1 %2 %3 %4 %5`) DO (
  echo %%F
  SET RESULT=%%F
  SET /a COUNT += 1
)

IF "%1" == "" (
  echo xd ^<directory name or pattern^>
) ELSE IF %COUNT%==0 (
  echo No directories match this pattern
) ELSE IF %COUNT%==1 (
  IF not "%RESULT%"=="" (
    cd %RESULT%
  )
) ELSE (
  echo.
  echo %COUNT% directories match this pattern
)
