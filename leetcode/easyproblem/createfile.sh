if [ $# -eq 0 ]; then
    echo "Usage: $0 <file_name_without_py_extension>"
    exit 1
fi
FILE_NAME=$1

echo "if __name__ == '__main__':" >> "${FILE_NAME}.py"
echo "    # Add your code here" >> "${FILE_NAME}.py"
