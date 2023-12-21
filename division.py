def division(nom, denom):
    if denom != 0:
        result = nom /denom
        return result
    else:
        return ValueError("dont divide by 0, silly.")
    
if __name__ == "__main__":
    print(division(5,4))
    print(division(5,0))