from __future__ import unicode_literals
import re
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bancos import BANCOS


ENQUADRAMENTO_FICAL = [
    ('LR',  'Lucro Real'),
    ('LP', 'Lucro Presumido'),
    ('SN', 'Simples Nacional'),
    ('SE', 'Simples Nacional, , excesso sublimite de receita bruta')
]

TIPO_PESSOA = [
    ('PF', 'Pessoa Fisica'),
    ('PJ', 'Pessoa Jurídica')
]

TIPO_TELEFONE = [
    ('FIX', 'Fixo'),
    ('CEL', 'Celular'),
    ('FAX', 'Fax'),
    ('OUT', 'Outro')

]

TIPO_ENDERECO = [
    ('UNi', 'Unico'),
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro')
]


UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('EX', 'EX'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

COD_UF = [
    ('12', 'AC'),
    ('27', 'AL'),
    ('16', 'AP'),
    ('13', 'AM'),
    ('29', 'BA'),
    ('23', 'CE'),
    ('53', 'DF'),
    ('32', 'ES'),
    ('EX', 'EX'),
    ('52', 'GO'),
    ('21', 'MA'),
    ('51', 'MT'),
    ('50', 'MS'),
    ('31', 'MG'),
    ('15', 'PA'),
    ('25', 'PB'),
    ('41', 'PR'),
    ('26', 'PE'),
    ('22', 'PI'),
    ('33', 'RJ'),
    ('24', 'RN'),
    ('43', 'RS'),
    ('11', 'RO'),
    ('14', 'RR'),
    ('42', 'SC'),
    ('35', 'SP'),
    ('28', 'SE'),
    ('17', 'TO'),
]



class Pessoa(models.Model):
    nome_razao_social = models.CharField(max_length=255)
    tipo_pessoa = models.CharField(max_length=2, choices=TIPO_PESSOA)
    incricao_municipal = models.CharField(max_length=32, null=True, blank=True)
    informacoes_adcionais = models.CharField(max_length=1055, null=True, blank=True)

    endereco_padrao = models.ForeignKey('cadastro.Endereco', 
                                        related_name='end_padrao', on_delete=models.CASCADE,
                                        null=True, blank=True)

    telefone_padrao = models.ForeignKey('cadastro.Telefone', 
                                        related_name='tel_padrao', on_delete=models.CASCADE,
                                        null=True, blank=True)

    site_padrao = models.ForeignKey('cadastro.Site',
                                    related_name='sit_padrao', on_delete=models.CASCADE,
                                    null=True, blank=True)

    email_padrao = models.ForeignKey('cadastro.Email',
                                    related_name='emai_padrao', on_delete=models.CASCADE,
                                    null=True, blank=True)

    banco_padrao = models.ForeignKey('cadastro.banco',
                                    related_name='ban_padrao', on_delete=models.CASCADE,
                                    null=True, blank=True)

    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_criacao = models.DateTimeField(editable=False)
    data_edicao = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Atualiza a data de criacao e ediçao
        if not self.data_criacao:
            self.data_criacao = timezone.now()
        self.data_edicao = timezone.now()

    return super(Pessoa, self).save(*args, **kwargs)



    @property
    def cpf_cnpj_apenas_digitos(self):
        if self.tipo_pessoa == 'pf':
            if self.pessoa_fis_info.cpf:
                return re.sub('[./-]', '', self.pessoa_fis_info.cpf)


        elif self.tipo_pessoa == 'PJ':
            if self.pessoa_jur_info.cnpj 
            return re.sub('[./-]', '',  serlf.pessoa_jur)info.cnpj)

        
        return ''


