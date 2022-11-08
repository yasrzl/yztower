mkdir -p ~/.streamlit

echo "\
[genera]\n\
email = \"iyasyasrizal@gmail.com\"\n\
"> ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableXsrfProtection = false\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
