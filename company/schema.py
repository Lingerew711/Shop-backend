import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id #for updating




# class CityNode(DjangoObjectType):
#     class Meta:
#         model = City
#         filter_fields = ['city_name']
#         interfaces = (graphene.relay.Node,)
# class TitleNode(DjangoObjectType):
#     class Meta:
#         model = Title
#         filter_fields = ['title_name']
#         interfaces = (graphene.relay.Node,)
# class EmployeeNode(DjangoObjectType):
#     class Meta:
#         model = Employee
#         filter_fields = [
#               'employee_name',
#               'employee_city__city_name',
#               'employee_title__title_name'
#                ]
#         interfaces = (graphene.relay.Node,)
# class Query(object):
#     city = graphene.relay.Node.Field(CityNode)
#     all_cities = DjangoFilterConnectionField(CityNode)
#     title = graphene.relay.Node.Field(TitleNode)
#     all_titles = DjangoFilterConnectionField(TitleNode)
#     employee = graphene.relay.Node.Field(EmployeeNode)
#     all_employees = DjangoFilterConnectionField(EmployeeNode)

# class CreateTitle(graphene.relay.ClientIDMutation):
#     title = graphene.Field(TitleNode)
#     class Input:
#         title_name = graphene.String()
#     def mutate_and_get_payload(root, info, **input):
#         title = Title(
#             title_name=input.get('title_name')
#         )
#         title.save()
    
#         return CreateTitle(title=title)

# class CreateEmployee(graphene.relay.ClientIDMutation):
#     employee = graphene.Field(EmployeeNode)
#     class Input:
#         employee_name = graphene.String()
#         employee_city = graphene.String()
#         employee_title = graphene.String()
#     def mutate_and_get_payload(root, info, **input):
#         employee = Employee(
#            employee_name=input.get('employee_name'),
#            employee_city=City.objects.get(
#               city_name=input.get('employee_city')),
#           employee_title=Title.objects.get(
#              title_name=input.get('employee_title'))
#         )
#         employee.save()
#         return CreateEmployee(employee=employee)

# class UpdateEmployee(graphene.relay.ClientIDMutation):
#     employee = graphene.Field(EmployeeNode)
#     class Input:
#         id = graphene.String()
#         employee_name = graphene.String()
#         employee_city = graphene.String()
#         employee_title = graphene.String()
#     def mutate_and_get_payload(root, info, **input):
#         employee = Employee.objects.get(
#             pk=from_global_id(input.get('id'))[1])
#         employee.employee_name = input.get('employee_name')
#         employee.employee_city = City.objects.get(
#             city_name=input.get('employee_city'))
#         employee.employee_title = Title.objects.get(
#             title_name=input.get('employee_title'))
#         employee.save()
#         return UpdateEmployee(employee=employee)

# class DeleteEmployee(graphene.relay.ClientIDMutation):
#     employee = graphene.Field(EmployeeNode)
#     class Input:
#         id = graphene.String()
#     def mutate_and_get_payload(root, info, **input):
#         employee = Employee.objects.get(
#             pk=from_global_id(input.get('id'))[1])
#         employee.delete()
#         return DeleteEmployee(employee=employee)


# class Mutation(graphene.AbstractType):
#     create_title = CreateTitle.Field()
#     create_employee = CreateEmployee().Field()
#     update_employee = UpdateEmployee().Field()
#     delete_employee = DeleteEmployee.Field()


class ProductNode(DjangoObjectType):
    class Meta:
        filter_fields = [
            "product_id", 
            "brand", 
            "product_name", 
            "date",
            "description", 
            "category", 
            "price", 
            "condition", 
            "delivery_available", 
            "discount", 
            "product_count"]
        model = Product
        interfaces = (graphene.relay.Node,)
    
    # @validates("image")
    # def validate_url(self, value):
    #     regex = re.compile(
    #         r'^(?:http|ftp)s?://'  # http:// or https://
    #         # domain...
    #         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    #         r'localhost|'  # localhost...
    #         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    #         r'(?::\d+)?'  # optional port
    #         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    #     if not re.match(regex, value):
    #         msg = u"Invalid image url."
    #         raise ValidationError(msg)


class WishListNode(DjangoObjectType):
    class Meta:
        filter_fields = ("wishlist_id", "product_id","product_name", "date")
        model = WishList
        interfaces = (graphene.relay.Node,)
        ordered = True
    # product = models.Nested(Product)


class CreateProduct(graphene.relay.ClientIDMutation):
    product = graphene.Field(ProductNode)
    class Input:
        product_id = graphene.Int()
        brand = graphene.String()
        product_name = graphene.String()
        date = graphene.Date()
        description = graphene.String()
        category = graphene.String()
        price = graphene.Float()
        condition = graphene.String()
        # image = graphene.String()
        delivery_available = graphene.Boolean()
        discount = graphene.Float()
        product_count = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        product = Product(
            product_id = input.get('product_id'),
            brand=input.get('brand'),
            product_name=input.get('product_name'),
            date = input.get('date'),
            description=input.get('description'),
            category=input.get('category'),
            price = input.get('price'),
            condition=input.get('condition'),
            # image=input.get('image'),
            delivery_available = input.get('delivery_available'),
            discount=input.get('discount'),
            product_count=input.get('product_count'),
           
        )
        product.save()
        return CreateProduct(product=product)

class UpdateProduct(graphene.relay.ClientIDMutation):
    product = graphene.Field(ProductNode)
    class Input:
        product_id = graphene.Int()
        brand = graphene.String()
        product_name = graphene.String()
        date = graphene.Date()
        description = graphene.String()
        category = graphene.String()
        price = graphene.Float()
        condition = graphene.String()
        # image = graphene.String()
        delivery_available = graphene.Boolean()
        discount = graphene.Float()
        product_count = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        product = Product.objects.get(
            pk=input.get('product_id'))
        product.product_id = input.get('product_id')
        product.brand = input.get('brand')
        product.product_name = input.get('product_name')
        product.date = input.get('date')
        product.description = input.get('description')
        product.category = input.get('category')
        product.price = input.get('price')
        product.condition = input.get('condition')
        product.delivery_available = input.get('delivery_available')
        product.discount = input.get('discount')
        product.product_count = input.get('product_count')
        product.save()
        return UpdateProduct(product=product)

class DeleteProduct(graphene.relay.ClientIDMutation):
    product = graphene.Field(ProductNode)
    class Input:
        product_id = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        product = Product.objects.get(
            pk=input.get('product_id'))
        product.delete()
        return DeleteProduct(product=product)

class DeleteWhishlist(graphene.relay.ClientIDMutation):
    wishlist = graphene.Field(WishListNode)
    class Input:
        wishlist_id = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        wishlist = WishList.objects.get(
            pk=input.get('wishlist_id'))
        wishlist.delete()
        return DeleteWhishlist(wishlist=wishlist)

class CreateWishlist(graphene.relay.ClientIDMutation):
    wishlist = graphene.Field(WishListNode)
    class Input:
        wishlist_id = graphene.Int()
        product_id = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        wishlist = WishList(
           wishlist_id=input.get('wishlist_id'),
           product_id=Product.objects.get(
              product_id=input.get('product_id')),
        )
        wishlist.save()
        return CreateWishlist(wishlist=wishlist)


class Query(object):
    product = graphene.relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)
    wishlist = graphene.relay.Node.Field(WishListNode)
    all_wishlists = DjangoFilterConnectionField(WishListNode)


class Mutation(graphene.AbstractType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
    delete_wishlist = DeleteWhishlist.Field()
    create_wishlist = CreateWishlist.Field()
    
    