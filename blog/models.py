#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categorie(models.Model):
	nom=models.CharField(max_length=30)
	def _str_(self):
		return self.nom

class Article(models.Model):
	titre=models.CharField(max_length=100)
	auteur=models.CharField(max_length=42)
	contenu=models.TextField(null=True)
	date=models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="date de parution")
	categorie=models.ForeignKey('Categorie')

	def _str_(self):
	
	

		return self.titre

class Produit(models.Model):
	nom=models.CharField(max_length=30)

	def _str_(self):
		return self.nom

class Vendeur(models.Model):
	nom=models.CharField(max_length=30)
	produit=models.ManyToManyField(Produit,through='Offre')

	def _str_(self):
		return self.nom

class Offre(models.Model):
	prix=models.IntegerField()
	produit=models.ForeignKey(Produit)
	vendeur=models.ForeignKey(Vendeur)

	def _str_(self):
		return "{0} vendu par {1}".format(self.produit, self_vendeur)

class Contact(models.Model):

    nom = models.CharField(max_length=255)

    adresse = models.TextField()

    photo = models.ImageField(upload_to="photos/")

    

    def __str__(self):

           return self.nom





