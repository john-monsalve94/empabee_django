import graphene
import graphql_jwt
from graphene_django import DjangoObjectType
from principal.models import *


class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        departamentos = graphene.Field(graphene.List('path.to.Departamentos'))
        fields = ("__all__")
        
        
class DepartamentoType(DjangoObjectType):
    class Meta:
        model = Departamentos
        pais = graphene.Field(Pais)
        fields = ("__all__")
        

class traerPaises(graphene.ObjectType):
    paises = graphene.List(PaisType)
    
    def resolve(self,info):
        paises = Pais.objects.all()
        return traerPaises(paises=paises)
        
class CreatePaisMutation(graphene.Mutation):
    class Arguments:
        nombre = graphene.String()
        codigo = graphene.Int()
    
    pais = graphene.Field(PaisType)
    
    def mutate(self,info,nombre,codigo):
        pais = Pais(nombre = nombre, codigo=codigo)
        pais.save()
        return CreatePaisMutation(pais=pais)
    
class DeletePaisMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()
    
    def mutate(self,info,id):
        pais = Pais.objects.get(pk=id)
        pais.delete()
        return DeletePaisMutation(message="Pais eliminado correctamente")
    
class UpdatePaisMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nombre = graphene.String()
        codigo = graphene.String()
    
    pais= graphene.Field(PaisType)
    
    def mutate(self,info,id,nombre,codigo):
        pais = Pais.objects.get(pk=id)
        pais.nombre = nombre
        pais.codigo = codigo
        pais.save()
        return UpdatePaisMutation(pais = pais)
    
class Query(graphene.ObjectType):
    traer_paises = graphene.List(PaisType)
    pais = graphene.Field(PaisType,id=graphene.ID())
    
    def resolve_paises(self, info):
        return Pais.objects.all()
    
    def resolve_pais(self,info,id):
        return Pais.objects.get(pk=id)
    
class Mutation(graphene.ObjectType):
    create_pais = CreatePaisMutation.Field()
    delete_pais = DeletePaisMutation.Field()
    update_pais = UpdatePaisMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    
schema=graphene.Schema(query=Query,mutation=Mutation)
        