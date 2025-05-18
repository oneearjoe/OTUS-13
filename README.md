# OTUS-13
# Run test
python -m pytest --alluredir allure-results

# Generate a report
allure serve allure-results
