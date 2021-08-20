import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id #for updating


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
        product_id = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        wishlist = WishList.objects.get(
            pk=input.get('product_id'))
        wishlist.delete()
        return DeleteWhishlist(wishlist=wishlist)

class CreateWishlist(graphene.relay.ClientIDMutation):
    wishlist = graphene.Field(WishListNode)
    class Input:
        product_id = graphene.Int()
    def mutate_and_get_payload(root, info, **input):
        wishlist = WishList(
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
    
    