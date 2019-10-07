# Strippend filename from an absolute path
# returns a Series
stripped_filename = df.filename.apply(lambda x : x.split("/")[-1]) #df -> Pandas dataframe

