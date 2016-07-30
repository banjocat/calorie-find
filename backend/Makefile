DATAZIP=sr28abbr.zip
URL=https://www.ars.usda.gov/SP2UserFiles/Place/12354500/Data/SR/SR28/dnload
TARGET=./calorie_find/calories/fixtures/food.json

all: ${TARGET}

data.txt: 
	echo "Getting data!"
	wget ${URL}/${DATAZIP}
	unzip ${DATAZIP}
	rm -rf ${DATAZIP}
	rm *.pdf
	mv ABBREV.txt data.txt
	echo "Data file created"

food_calorie.json: data.txt
	python to_fixture.py data.txt

${TARGET}: food_calorie.json
	mv food_calorie.json ${TARGET}


clean:
	rm -rf data.txt
	rm -rf food_calorie.json

