git push origin master
source .env
cd deploy_tools
fab deploy:host=good_tests@good-tests.com
