set -e

test_project_name="toast"

rm -rf "$test_project_name";
cookiecutter lib_template --no-input;
cd "$test_project_name" || exit;
nox;
cd ..
