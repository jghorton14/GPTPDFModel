# mychatbot
This is a very basic example of extending ChatGPT with LlamaIndex to get around our data input limitation (~2k word limit). With LlamaIndex, it can connect your existing data sources and types with available data connectors, for example (APIs, PDFs, docs, SQL, etc.)

LlamaIndex will transform the original document data into a query-friendly vectorized index. It will utilize this index to find the most pertinent sections based on how closely the query and data match.

In this example, we are passing in a Master Gardener PDF.

## To Build
```
conda env create --file environment.yml
```

## To Run
```
python3 main.py
```

## Example Questions
- What are ground covers?
```
The original answer already provides a thorough definition of ground covers, mentioning their low-growing nature and functions, such as controlling erosion, filling narrow areas, and thriving in shade or temperature extremes. However, the new context adds details regarding the maintenance needs of ground covers, which can be significant and time-consuming for the first one to three years until the plants become established. Ground covers require weed and plant invader control through cultivation, fertilization, irrigation, and disease and pest control. Failure to address these maintenance factors can result in disappointing outcomes in achieving good ground cover planting. Additionally, the context notes that ground covers can be useful in areas where paving, lawn, or cultivated beds are not desirable, such as newly cut banks, slopes greater than 12 percent, and areas around buildings where they reduce heat, glare, noise, and dust. Therefore, the original answer remains accurate, but can be refined by adding details on the maintenance needs, benefits, and limitations of ground covers.
```
- What are vines?
```
Vines are plants that develop long trailing stems that can grow along the ground or need support from another plant or structure, providing erosion control for banks while holding the soil in place. They offer diverse visual qualities, such as rich foliage texture, decorative growth habit, and beautiful flowers. Vines are generally segregated into three groups depending on how they climb, including twining, adhesive, and winding. Different vine species twine in different directions, and knowing how each vine climbs can be helpful in providing proper support. Without proper support and care, most vines will quickly revert to a tangled mass of foliage on the ground.
```
- How do I transplant native trees?
```
To successfully transplant native trees, it is important to understand the environment in which they naturally grow and duplicate that environment on the new planting site. Factors to consider include light, soil moisture, and soil acidity. Soil pH should be adjusted if necessary, and soil moisture and type should match the plant's natural environment. Root pruning should be done by dividing the circumference of the root area to be dug into six segments, and pruning with a sharp spade every other segment two years prior to transplanting, and the remaining segments the year prior to transplanting. Transplant during the dormant season, and dig a hole no deeper and 6 to 12 inches wider than the root system. Refill with a mixture of enough existing and native soil of the plant to accommodate the root ball or bare-root system. Set the plants a few inches higher than when growing in the woods and mulch with approximately 2 inches of decayed sawdust, leaf mold, or other available materials. Stake using either the 2 or 3-stake method to ensure a straight trunk and to prevent small plants from being stepped on. Do not use high nitrogen fertilizer at the time of planting. Adequate soil moisture is critical for several months after transplanting. Water only when necessary, and avoid overwatering, which can result in sure death, making sure to soak the ground thoroughly. An initial pruning may be needed immediately after planting, removing only broken or damaged branches. Since pruning reduces the leaf area, which produces photosynthates for root growth, it is generally more successful to avoid heavy pruning at planting, if possible, and to ensure the plants are well-watered during their first year or two in the ground.
```