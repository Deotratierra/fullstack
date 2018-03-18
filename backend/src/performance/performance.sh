#/bin/sh

            # Variables
VERBOSE=1
DEBUG=0

ITER=5  # Number of iterations for each example

LANGS_OFF=""  # Languages deactivated in comma separated string

# Machine information
SYS_NAME=$(python3 -c "import platform;print(platform.platform());" 2>&1)
SYS_VERSION=$(python3 -c "import platform;print(platform.version());" 2>&1)
SYS_MACHINE=$(python3 -c "import platform;print(platform.machine());" 2>&1)
SYS_CPU_NUMBER=$(python3 -c "import multiprocessing as mp;print(mp.cpu_count());" 2>&1)


# Flags
CONSTS_SHOWN=0

# Store info about all the languages
#   [0]: Readable language name
#   [1]: Extension
#   [2]: Execution command
#   [3]: Build command
#   [4]: Clean command
languages_map=( \
    '("Python3" "py" "python3")' \
    '("Golang" "go" "./" "go build")' \
    '("NodeJS" "js" "node")' \
    '("Ruby" "rb" "ruby")' \
    '("Cython" "pyx" "python3" "sudo python3 ../setup/pyx/setup.py install")' \
    '("C" "c" "./")' \
    '("C++" "cpp" "./")' \
    '("Bash" "sh")' \
)
n_languages=${#languages_map[@]}

            # Functions
: '
    Shows comparation suite title

    Args:
        $1: Redable title of comparations suite.
'
function title() {
    printf "Comparation between languages - $1\n\n"
}

function separator() {
    printf "__________________________________________\n\n"
}


: '
    Time execution of a command and shows it
        with milliseconds format.

    Args:
        $1: Command to be executed.
        $2: Readable language name of the command
'
function time_ms() {
    ts=$(date +%s%N) ; `$1` ; tt=$((($(date +%s%N) - $ts)/1000000)) ; printf "%d" "$tt"
}


: '
    Run a suite of performance comparations tests.

    Args:
        $1: Name of the file being executed.
        $2: Mode of count milliseconds elapsed.
              You can use "media" or "sum".
        $>=3: Arguments passed to script at execution.
'
function perf_suite() {

    # Show DEBUG options:
    if [[ $VERBOSE -eq 1 && $CONSTS_SHOWN -eq 0 ]]; then
        printf "            VERBOSE = 1\n"
        printf "            DEBUG = $DEBUG\n\n"
        printf "            ITER = $ITER\n"
        separator
        CONSTS_SHOWN=1
    fi

    # File to be executed (all langs the same name)
    source_file="$1"

    # File to store results
    if [ -f "$source_file.json" ]; then
        rm "$source_file.json"  # Rewrite file
    fi

    # Information about machine
    printf "{\n    \"sysname\": \"$SYS_NAME\"," > "$source_file.json"
    printf "\n    \"sysversion\": \"$SYS_VERSION\"," >> "$source_file.json"
    printf "\n    \"machine\": \"$SYS_MACHINE\"," >> "$source_file.json"
    printf "\n    \"cpu\": $SYS_CPU_NUMBER," >> "$source_file.json"
    printf "\n    \"iter\": $ITER," >> "$source_file.json"

    # Arguments matrix
    ARGS_MATRIX="\n    \"args\": ["

    for arg in $2; do
        ARGS_MATRIX="$ARGS_MATRIX$arg, "
    done

    ARGS_MATRIX="${ARGS_MATRIX::-2}],"
    printf "$ARGS_MATRIX" >> "$source_file.json"

    # Start storing results
    printf "\n    \"benchs\": [\n" >> "$source_file.json"


    # Iterate over all languages extensions
    for _data in "${languages_map[@]}"; do
        eval "data=$_data"
        LANG="${data[0]}"
        EXT="${data[1]}"
        EXEC="${data[2]}"
        BUILD="${data[3]}"
        CLEAN="${data[4]}"

        if [[ $VERBOSE -eq 1 ]]; then
            echo "- $LANG"
        fi

        # Skip languages with missing files
        EXTENSIONS=(`for f in *.*; do printf "%s," "${f##*.}"; done | sort -u 2>&1`)
        EXTENSIONS=(`printf '%s\n' "${EXTENSIONS//json/}" 2>&1`)
        EXTENSIONS=(`printf '%s\n' "${EXTENSIONS//$LANGS_OFF/}" 2>&1`) # ALso off languages deactivated
        if [[ $EXTENSIONS != *"$EXT,"* ]]; then
            if [[ $DEBUG -eq 1 ]]; then
                printf "Skipping extension '$EXT'.\n\n"
            fi
            continue
        fi

        # Prepare code depending on language
        if [[ $EXT = "pyx" ]]; then
            EXEC="$EXEC cy_$source_file.py"
            BUILD="$BUILD $source_file"
            CLEAN="sudo rm -rf build/ dist/ fib.egg-info/;mv cy$source_file.pyx $source_file.pyx;sudo rm cy$source_file.c"
        elif [[ "(py js rb)" == *"$EXT"* ]]; then
            # Python, NodeJS
            EXEC="$EXEC $source_file.$EXT"
        elif [[ $EXT = "go" ]]; then
            # Golang
            EXEC="$EXEC$source_file"
            BUILD="$BUILD $source_file.$EXT"
            CLEAN="rm $source_file"
        elif [[ $EXT = "c" || $EXT = "cpp" ]]; then
            if [[ $EXT = "c" ]]; then
                compiler="gcc"
            else
                compiler="g++"
            fi
            EXEC="$EXEC$source_file"
            BUILD="$compiler $source_file.$EXT -o $source_file"
            CLEAN="rm $source_file"
        elif [[ $EXT = "sh" ]]; then
            EXEC="bash $source_file.sh"
        fi


        # Build steps
        if [[ $BUILD != "" ]]; then
            if [ $DEBUG -eq 1 ]; then
                echo "              build: $BUILD"
            fi
            eval $BUILD
            if [[ $? -ne 0 ]]; then
                printf "Error building example for $LANG\n\n"
                continue
            fi
        fi

        # Execution
        #    Number of executions
        n_execs=$(echo "$2" | awk -F" " '{print NF-1}' 2>&1)
        n_execs=$(expr $n_execs + 1)

        if [ $DEBUG -eq 1 ]; then
            echo "              exec: $EXEC"
        fi

        JSON="       {\"language\": \"$LANG\","
        JSON="$JSON\n        \"results\": ["

        for args in $2; do
            # For every iteration
            JSON="$JSON["
            for i in $(seq 1 $ITER); do
                result=$(time_ms "$EXEC $args" 2>&1) # Execution
                JSON="$JSON$result, "
            done

            JSON="${JSON::-2}],"

        done

        JSON="${JSON::-1}]},"
        echo -e "$JSON" >> "$source_file.json"

        # Clean steps
        if [[ $CLEAN != "" ]]; then
            if [[ $DEBUG -eq 1 ]]; then
                echo "              clean: $CLEAN"
            fi
            eval $CLEAN
        fi
        if [[ $DEBUG -eq 1 ]]; then
            echo
        fi
    done
    JSON="${JSON::-1}\n    ]\n}"
    echo -e "$JSON" >> "$source_file.json"

    separator
    echo " -> Suite $source_file.* execution ended."

    if [[ $DEBUG -eq 1 ]]; then
        echo "Producing statistics..."
    fi
    python3 ../stats.py "$source_file"
    if [[ $DEBUG -eq 1 ]]; then
        echo "Statistics built."
    fi
}
