#/bin/sh

            # Variables
VERBOSE=1
DEBUG=0

ITER=5  # Number of iterations for each example

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
        $>=2: Arguments passed to script at execution.
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
    RESULTS_FILE="$source_file.json"
    if [ -f $RESULTS_FILE ]; then
        rm $RESULTS_FILE  # Rewrite file
    fi
    echo "[" > $RESULTS_FILE


    # Iterate over all languages extensions
    ilang=1
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
            BUILD=". $source_file.sh"
            EXEC="$source_file"
        fi


        # Build steps
        if [[ $BUILD != "" ]]; then
            if [ $DEBUG -eq 1 ]; then
                echo "              build: $BUILD"
            fi
            eval $BUILD
        fi

        # Execution
        #    Number of executions
        n_execs=$(echo "$2" | awk -F" " '{print NF-1}' 2>&1)
        n_execs=$(expr $n_execs + 1)

        if [ $DEBUG -eq 1 ]; then
            echo "              exec: $EXEC"
        fi

        JSON_LANG_RESULT="    {\n        \"language\": \"$LANG\",\n        \"results\": [\n"

        i=1
        for args in $2; do
            # Total results for all iterations
            result=0
            # For every iteration
            for i in $(seq 1 $ITER); do
                partial_result=$(time_ms "$EXEC $args" 2>&1)
                result=$(($result + $partial_result))
            done
            result=$((result/$ITER))

            # Store results in JSON file
            JSON_LANG_RESULT="$JSON_LANG_RESULT            {\"args\": [$args], \"result\": $result}"
            if [[ $i -ne $n_execs ]]; then
                JSON_LANG_RESULT="$JSON_LANG_RESULT,"
            fi
            JSON_LANG_RESULT="$JSON_LANG_RESULT\n"
            i=$(expr $i + 1)
        done
        JSON_LANG_RESULT="$JSON_LANG_RESULT        ]\n    }"
        if [[ $ilang -ne $n_languages ]]; then
            JSON_LANG_RESULT="$JSON_LANG_RESULT,"
        fi
        echo -e "$JSON_LANG_RESULT" >> $RESULTS_FILE

        # Clean steps
        if [[ $CLEAN != "" ]]; then
            if [ $DEBUG -eq 1 ]; then
                echo "              clean: $CLEAN"
            fi
            eval $CLEAN
        fi
        if [ $DEBUG -eq 1 ]; then
            echo
        fi

        # Enumerate languages
        ilang=$(expr $ilang + 1)
    done
    separator
    echo -e "]" >> $RESULTS_FILE

    echo " -> Suite $source_file.* execution ended."
}
