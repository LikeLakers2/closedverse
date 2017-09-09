from django.conf.urls import url

from . import views

username = r'(?P<username>[A-Za-z0-9-._]+)'
community = r'(?P<community>[0-9]+)'
post = r'(?P<post>[0-9]+)'
comment = r'(?P<comment>[0-9]+)'

app_name = 'main'
urlpatterns = [
	url(r'^^$|^communities$|^index.*$$', views.community_list, name='community-list'),
	url(r'login/$', views.login_page, name='login'),
	url(r'signup/$', views.signup_page, name='signup'),
	url(r'reset/$', views.forgot_passwd, name='forgot-passwd'),
	url(r'logout/$', views.logout_page, name='logout'),
	url(r'settings/profile$', views.profile_settings, name='profile-settings'),
	url(r'users/'+ username +'\.follow\.json$', views.user_follow, name='user-follow'),
	url(r'users/'+ username +'\.unfollow\.json$', views.user_unfollow, name='user-unfollow'),
	url(r'users/'+ username +'$', views.user_view, name='user-view'),
	url(r'users/'+ username +'/posts$', views.user_posts, name='user-posts'),
	url(r'users/'+ username +'/yeahs$', views.user_yeahs, name='user-yeahs'),
	url(r'users/'+ username +'/following$', views.user_following, name='user-following'),
	url(r'users/'+ username +'/followers$', views.user_followers, name='user-followers'),
	url(r'users/'+ username +'/friends$', views.user_friends, name='user-friends'),
	
	url(r'users/'+ username +'/friend\.new$', views.user_friendrequest_create, name='user-fr-create'),
	url(r'users/'+ username +'/friend\.accept$', views.user_friendrequest_accept, name='user-fr-accept'),
	url(r'users/'+ username +'/friend\.reject$', views.user_friendrequest_reject, name='user-fr-reject'),
	url(r'users/'+ username +'/friend\.cancel$', views.user_friendrequest_cancel, name='user-fr-cancel'),
	url(r'users/'+ username +'/friend\.delete$', views.user_friendrequest_delete, name='user-fr-delete'),
	
	url(r'origin', views.origin_id, name='origin-id-get'),
	
	url(r'communities/'+ community +'$', views.community_view, name='community-view'),
	url(r'communities/(?P<tag>[a-z]+)$', views.special_community_tag, name='special-community-tag'),
	url(r'communities/'+ community +'/posts$', views.post_create, name='post-create'),
	# Some of these NAMES (not patterns) are hardcoded into models.py
	url(r'posts/'+ post +'$', views.post_view, name='post-view'),
	url(r'posts/'+ post +'/yeah$', views.post_add_yeah, name='post-add-yeah'),
	url(r'posts/'+ post +'/yeah\.delete$', views.post_delete_yeah, name='post-delete-yeah'),
	url(r'posts/'+ post +'/comments$', views.post_comments, name='post-comments'),
	url(r'posts/'+ post +'/comments$', views.post_comments, name='post-comments'),
	url(r'posts/'+ post +'/change$', views.post_change, name='post-change'),
	url(r'posts/'+ post +'/profile$', views.post_setprofile, name='post-set-profile'),
	url(r'posts/'+ post +'/profile\.no', views.post_unsetprofile, name='post-unset-profile'),
	url(r'posts/'+ post +'\.rm$', views.post_rm, name='post-rm'),
	url(r'comments/'+ comment +'$', views.comment_view, name='comment-view'),
	url(r'comments/'+ comment +'/yeah$', views.comment_add_yeah, name='comment-add-yeah'),
	url(r'comments/'+ comment +'/yeah\.delete$', views.comment_delete_yeah, name='comment-delete-yeah'),
	url(r'comments/'+ comment +'/change$', views.comment_change, name='comment-change'),
	url(r'comments/'+ comment +'\.rm$', views.comment_rm, name='comment-rm'),

	url(r'notif_count\.json$', views.check_notifications, name='check-notifications'),
	url(r'notifications/?$', views.notifications, name='notifications'),
	url(r'notifications/friend_requests/?$', views.friend_requests, name='friend-requests'),
	url(r'notifications/set_read$', views.notification_setread, name='set-read'),
	url(r'notifications/(?P<notification>[0-9a-f\-]+)\.rm$', views.notification_delete, name='notification-delete'),
	
	url(r'activity/?$', views.activity_feed, name='activity'),
	url(r'users\.search$', views.user_search, name='user-search'),
	url(r'messages/?$', views.messages, name='messages'),
	url(r'messages/'+ username +'$', views.messages_view, name='messages-view'),
	url(r'messages/'+ username +'/read$', views.messages_read, name='messages-read'),
	
	url(r'lights$', views.set_lighting, name='set-lighting'),
	url(r'complaints$', views.help_complaint, name='complaints'),
	url(r'meta/rules/?$', views.help_rules, name='help-rules'),
	url(r'meta/faq/?$', views.help_faq, name='help-faq'),
	url(r'meta/legal/?$', views.help_legal, name='help-legal'),
	url(r'meta/contact/?', views.help_contact, name='help-contact')
]
