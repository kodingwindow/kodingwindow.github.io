CALL pip install -r requirements.txt
CALL gem install jekyll bundler
CALL bundle config set --local path vendor/bundle
CALL bundle install
CALL bundle update --bundler
CALL bundle update
CLS
CALL bundle exec jekyll serve