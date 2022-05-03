# install from pip
pip install ryu

# Update git submodule
git submodule update --init --recursive
cd ryu; pip install .

# Optional Requirements
pip install -r tools/optional-requires

# Prerequisites
# install as super user
sudo apt install gcc python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev

