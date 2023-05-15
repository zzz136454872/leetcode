# reverse [l,r]

# d = abs(a[l]-a[r+1])+abs(a[l-1]-a[r])-abs(a[l]-a[l-1])-abs(a[r+1]-a[r])
# d = max(a[l]-a[r+1],a[r+1]-a[l])+max(a[l-1]-a[r],a[r]-a[l-1])+max(a[l]-a[l-1],a[l-1]-a[l])+max(a[r+1]-a[r],a[r]-a[r+1])

# a[l]>a[r+1] and a[l-1]>a[r] and a[l]>a[l-1]
