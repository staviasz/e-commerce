{% extends 'base.html' %}
{% load omfilters %}

{% block titulo %}Resumo da compra | {% endblock %}

{% block conteudo %}

<div class="row mb-5">
    <div class="col-lg">
        <h2>Resumo da sua compra</h2>

        <p class="lead">Dados do usuário</p>
        <p>Caso precise editar, <a href="{% url 'perfil:criar' %}">clique aqui</a></p>
        <dl class="row">
            <dt class="col-lg-2">Nome:</dt>
            <dd class="col-lg-4">{{ usuario.first_name }}</dd>
            <dt class="col-lg-2">Sobrenome:</dt>
            <dd class="col-lg-4">{{ usuario.last_name }}</dd>

            <dt class="col-lg-2">Idade:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.idade }}</dd>
            <dt class="col-lg-2">Nascimento:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.data_nascimento }}</dd>

            <dt class="col-lg-2">CPF:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.cpf }}</dd>
            <dt class="col-lg-2">E-mail:</dt>
            <dd class="col-lg-4">{{ usuario.email }}</dd>
        </dl>

        <p class="lead">Dados de endereço</p>
        <p>Caso precise editar, <a href="{% url 'perfil:criar' %}">clique aqui</a></p>
        <dl class="row">
            <dt class="col-lg-2">Endereço:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.endereco }}</dd>
            <dt class="col-lg-2">Número:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.numero }}</dd>

            <dt class="col-lg-2">Complemento:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.complemento }}</dd>
            <dt class="col-lg-2">Nascimento:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.bairro }}</dd>

            <dt class="col-lg-2">Cidade:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.cidade }}</dd>
            <dt class="col-lg-2">Estado:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.estado }}</dd>

            <dt class="col-lg-2">CEP:</dt>
            <dd class="col-lg-4">{{ usuario.perfil.cep }}</dd>
        </dl>
    </div>
</div>



<div class="row mt-3">
    <div class="col">
        <h3>Resumo do carrinho</h3>
        <p class="lead">Os produtos, quantidades e preços que você escolheu.</p>

        {% include 'parciais/_carrinho.html' %}
    </div>

</div>
<div class="row mt-3">
    <div class="col">
        <p class="lead text-center"><span class="font-weight-bold">Total do carrinho:</span>
            {{ carrinho|cart_totals|formata_preco }}</p>
    </div>
</div>

<div class="row">
    <div class="col">
        <a class="btn btn-block btn-primary btn-lg" href="{% url 'pedido:salvarpedido' %}">
            Realizar pedido e pagar
        </a>
    </div>
</div>


{% endblock %}
