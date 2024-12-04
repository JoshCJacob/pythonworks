
arr=[10,11,15,13,20,25]

#read search elemnt

search_element=int(input("Enter the Number:"))

arr.sort()

low=0

upp=len(arr)-1

is_present=False

while(low<=upp):

    #find mid

    mid=(low+upp)//2

    #case 1

    if search_element==arr[mid]:
     
     is_present=True

     break

    elif search_element<arr[mid]:

      upp=mid-1

    elif search_element>arr[mid]:

     low=mid+1

print(is_present)
