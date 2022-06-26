def validate_request(request, disk):
    '''
    Function to check whether the input requests are valid or not
    
    ## Returns
    - True if sectors are valid
    - False otherwise
    '''
    for i in request:
        #Negative sector or sector beyond disk boundary
        if i<0 or i>=disk:
            return False
    return True

