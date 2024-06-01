set -e

test_project_name="toast_test"

rm -rf "$test_project_name";
cookiecutter lib_template --no-input;
cd "$test_project_name" || exit;
just test;
just ruff-check;
just mypy;
cd ..
