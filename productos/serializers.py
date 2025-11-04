from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
    
class ProductoSerializer(serializers.ModelSerializer):
    # Esto nos permite mostrar el nombre de la categoría en el GET
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 
            'nombre', 
            'descripcion', 
            'precio', 
            'imagen', 
            'disponible', 
            'categoria',          # Para POST/PATCH (acepta un ID)
            'categoria_nombre'    # Para GET (muestra el nombre)
        ]
        extra_kwargs = {
            'imagen': {'required': False, 'allow_null': True},
            'categoria': {'required': False, 'allow_null': True, 'write_only': True}
        }

    # Sobreescribimos 'to_representation' para incluir 'categoria' en el GET
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Añadimos el ID de la categoría al JSON que enviamos (para el GET)
        representation['categoria'] = instance.categoria_id
        return representation