import instaloader

username = "gamek.0105"
L = instaloader.Instaloader()
profile=instaloader.Profile.from_username(L.context, username)

# print("biography:", profile.biography)
# print("biography_hashtags:", profile.biography_hashtags)
# print("biography_mentions:", profile.biography_mentions)
# print("blocked_by_viewer:", profile.blocked_by_viewer)
# print("business_category_name:", profile.business_category_name)
# print("external_url:", profile.external_url)
# print("followed_by_viewer:", profile.followed_by_viewer)
# print("followees:", profile.followees)
# print("followers:", profile.followers)
# print("follows_viewer:", profile.follows_viewer)
# print("full_name:", profile.full_name)
# print("igtvcount:", profile.igtvcount)
# print("is_business_account:", profile.is_business_account)
# print("is_private:", profile.is_private)
# print("is_verified:", profile.is_verified)
# print("mediacount:", profile.mediacount)
# print("requested_by_viewer:", profile.requested_by_viewer)
# print("userid:", profile.userid)
# print("username:", profile.username)

avatar_url = profile.profile_pic_url
L.download_pic(avatar_url, 'avatar.png')

class obj(object):
    def __init__(self, d):
        for k, v in d.items():
            if isinstance(k, (list, tuple)):
                setattr(self, k, [obj(x) if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, obj(v) if isinstance(v, dict) else v)