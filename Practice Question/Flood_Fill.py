def solve(image , sr, sc, color):
    og_color=image[sr][sc]
    if og_color== color:
        return image
    image[sr][sc]=color
    if sr>0 and image[sr-1][sc]==og_color:
        solve(image,sr-1,sc,color)
    if sc>0 and image[sr][sc-1]==og_color:
        solve(image,sr,sc-1, color)
    if sr<len(image)-1 and image[sr+1][sc]==og_color:
        solve(image,sr+1,sc, color)
    if sc<len(image[0])-1 and image[sr][sc+1]==og_color:
        solve(image,sr,sc+1, color)
    return image



print([[3,3],
[1,1,1],
[1,1,0],
[1,0,1]],1,1,2)