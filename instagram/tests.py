from django.test import TestCase
from .models import Follow,Comments,Post,Profile,User
import datetime as dt


class PostTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = User(username='Mugera')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="good_picture.png")
        self.post = Post(name="views",caption="Nyc views",user=self.user_profile)
        
    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))
            
    def test_save_post(self):
        self.post.save_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)>0)
        
    def test_delete_post(self):
        self.post.save_post()
        self.post.delete_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)==0)
        
    def test_update_caption(self):
        self.post.save_post()
        self.post.update_post_caption(self.post.id,'test')
        updated= Post.objects.get(caption='test')
        self.assertEqual(updated.caption,'test')
            
        

class CommentsTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = User(username='Mugera')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="good_picture.png")
        self.post = Post(name="views",caption="Nyc views",user=self.user_profile)
        self.post.save()
        self.comment = Comments(comment="Awsome",post=self.post,user=self.user)
        
    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()
        Comments.objects.all().delete()
        Profile.objects.all().delete()
        
            
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))
            
    def test_save_comment(self):
        self.comment.save_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)>0)
        
    def test_delete_comment(self):
        self.comment.save_comment()
        self.comment.delete_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)==0)
        
        
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = User(username='Mugera')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="good_picture.png")
      
        
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
   
            
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_user_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_user_profile(self):
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)
        





        
    # def test_save_method(self):
    #     self.Comment.save_Comment()
    #     categories= Comment.objects.all()
    #     self.assertTrue(len(categories) > 0)
    
    # def test_delete_method(self):
    #     self.Comment.save_Comment()
    #     self.Comment.delete_Comment()
    #     categories = Comment.objects.all()
    #     self.assertTrue(len(categories) == 0)
       
    # def test_update_Comment(self):
    #     self.Comment.save_Comment()
    #     new_name="Fam"
    #     self.Comment.update_Comment(self.Comment.id,new_name)
    #     update = Comment.objects.get(name="Fam")
    #     self.assertEquals(update.name,"Fam")
        
        
# class LocationTestClass(TestCase):
#     #setup method
#     def setUp(self):
#         self.location = Location(name='Mombasa')
#         self.location.save_location()
        
#     def tearDown(self):
#         Location.objects.all().delete()
    
#     def test_instance(self):
#         self.assertTrue(isinstance(self.location,Location))
        
#     def test_save_method(self):
#         self.location.save_location()
#         locations= Location.objects.all()
#         self.assertTrue(len(locations) > 0)
        
#     def test_delete_method(self):
#         self.location.save_location()
#         self.location.delete_location()
#         locations = Location.objects.all()
#         self.assertTrue(len(locations) == 0)
    
#     def test_update_location(self):
#         self.location.save_location()
#         new_name="Nyeri"
#         self.location.update_location(self.location.id,new_name)
#         update = Location.objects.get(name='Nyeri')
#         self.assertEquals(update.name,"Nyeri")
        
    
        
# class ImageTestClass(TestCase):
#     #setup method
#     def setUp(self):
#         self.location = Location(name='Mombasa',)
#         self.location.save_location()
#         self.Comment = Category(name='Family')
#         self.category.save_category()
#         self.new_image = Image(name='Art',description="Street Art" ,location=self.location,category=self.category)
#         self.new_image.save_image()
        
        
#     def tearDown(self):
#         Image.objects.all().delete()
#         Location.objects.all().delete()
#         Category.objects.all().delete()
    
#     def test_image_instance(self):
#         self.assertTrue(isinstance(self.new_image,Image))
        
#     def test_save_image(self):
#         self.new_image.save_image()
#         images=Image.objects.all()
#         self.assertTrue(len(images)>0)
        
#     def test_delete_image(self):
#         self.new_image.delete_image()
#         images=Image.objects.all()
#         self.assertTrue(len(images)==0)
        
#     def test_update_image(self):
#         self.new_image.save_image()
#         self.new_image.update_image_name(self.new_image.id,'test')
#         updated= Image.objects.get(name='test')
#         self.assertEqual(updated.name,'test')
            
#     def test_get_image_by_id(self):
#         self.new_image.save_image()
#         image_found=self.new_image.get_image_by_id(self.new_image.id)
#         self.assertTrue(len(image_found)>0)
        
#     def test_filter_by_location(self):
#         self.new_image.save_image()
#         found_images = self.new_image.filter_by_location(location='Mombasa')
#         self.assertTrue(len(found_images) == 1)
        
#     def test_search_image_by_category(self):
#         self.new_image.save_image()
#         found_img = self.new_image.search_by_category('Family')
#         self.assertTrue(len(found_img) == 1)


