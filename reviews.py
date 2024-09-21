# add your code here
import pandas as pd

reviews = pd.read_csv(r'C:\Users\kylev\Documents\GitHub\wine-reviews-exercise-KyleVCosta\data\winemag-data-130k-v2.csv.zip')


# reviews_country = reviews.country.value_counts()
function_dictionary = {'description': 'count', 'points':'mean'}

refined_df = reviews.groupby('country').aggregate(function_dictionary).sort_values(by='description', ascending=False)



refined_df2 = pd.DataFrame(refined_df)
refined_df3 = refined_df2.rename(columns={'description': 'count'})
refined_df3['points'] = refined_df3['points'].round(1)

print(refined_df3)

refined_df3.to_csv(r'C:\Users\kylev\Documents\GitHub\wine-reviews-exercise-KyleVCosta\data\reviews-per-country.csv')
