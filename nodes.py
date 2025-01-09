class StringListSplitter:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"string_list": ("STRING", {"multiline": True})}}
    
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    FUNCTION = "split_string_list"
    CATEGORY = "utils"

    def split_string_list(self, string_list):
        # 分割字符串并过滤掉空行
        list_items = [item.strip() for item in string_list.split('\n') if item.strip()]
        
        # 确保列表至少有3个元素，不足的用None填充
        output = list_items[:3] + [None] * (3 - len(list_items))
        
        return tuple(output)