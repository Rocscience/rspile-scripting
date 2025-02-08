@echo off
setlocal enabledelayedexpansion

:: Load environment variables from the .env file
for /f "tokens=1,2 delims==" %%i in ('type ".env"') do (
    set %%i=%%j
)

:: Navigate to the target folder
set "target_path=%PATH_TO_RSPILE_PYTHON_REPO%\docs\example_code"
if exist "%target_path%" (
    cd /d "%target_path%"
    echo Changed directory to %target_path%
) else (
    echo Target path "%target_path%" does not exist. Exiting.
    endlocal
    exit /b 1
)

:: Process Python files in the target directory
for %%f in (*.py) do (
    python "%%f" > "%%~nf_result.txt"
    
    if !ERRORLEVEL! EQU 0 (
        echo Successfully finished processing %%f
    ) else (
        python "%%f" > "%%~nf_result.txt" 2> "%%~nf_error.log"
        echo Failed to process %%f. See %%~nf_error.log for details.
    )
)

endlocal