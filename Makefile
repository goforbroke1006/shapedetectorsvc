TEST_PATH=./tests/

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}

setup:
	bash bin/setup-local.sh

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

run: clean-pyc
	python main.py --image ./assets/crosses.jpg

docker-run:
	echo "Coming soon"