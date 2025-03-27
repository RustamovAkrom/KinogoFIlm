import facebook


class Facebook:

    @staticmethod
    def validate(auth_token):
        try:
            graph = facebook.GraphAPI(access_token=auth_token)
            profile = graph.request("/me?fields=id,name,email")
            return profile
        
        except facebook.GraphAPIError as e:
            print(f"Facebook API Error: {e}")
            return {"error": str(e)}
        
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return "The Token is invalid or expired."