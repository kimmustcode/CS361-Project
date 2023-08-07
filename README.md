# CS361-Project

Kim Manske 

Description: Workout that records, saves and visualizes your workout data.



**Communication Contract**

1. How to request data.
    Data is requested by redirecting the client with
   
   return redirect("http://127.0.0.1:5000/display_info?")

3. How to Recieve Data 
   Flask return sends data directly back to the destination 
    
   return cleaned_data

   If the data is changed to be json format then 

   return request.get_json()

![image](https://github.com/kimmustcode/CS361-Project/assets/139509384/0a0a32b9-7bae-4545-b254-6bcd77abbfa7)
