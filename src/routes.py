# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.models_def import db, Car, CarStatus, CategoriaEnum

car_bp = Blueprint("car_bp", __name__, template_folder="../templates")

@car_bp.route("/")
def index():
    cars = Car.query.all()
    return render_template("index.html", cars=cars, car_status=CarStatus)

@car_bp.route("/painel")
def publico():
    cars = Car.query.all()
    return render_template("painel.html", cars=cars, car_status=CarStatus)

@car_bp.route('/add', methods=['POST'])
def add_car():
    prefixo = request.form['prefixo']
    status = request.form['status']
    categoria = request.form.get('categoria', 'FRETAMENTO')
    observacao = request.form.get('observacao', '')

    try:
        novo_carro = Car(
            prefixo=prefixo,
            status=CarStatus[status],  # Corrigido aqui
            categoria=CategoriaEnum[categoria],  # Usa o enum correto
            observacao=observacao
        )
        db.session.add(novo_carro)
        db.session.commit()
        return redirect(url_for('car_bp.index'))
    except Exception as e:
        db.session.rollback()
        print("Erro ao adicionar carro:", e)
        return "Erro ao adicionar carro", 500

@car_bp.route("/edit/<int:car_id>", methods=['POST'])
def edit_car(car_id):
    car = Car.query.get_or_404(car_id)
    car.prefixo = request.form['prefixo']
    car.status = CarStatus[request.form['status']]  # Corrigido aqui
    car.categoria = CategoriaEnum[request.form['categoria']]
    car.observacao = request.form.get('observacao', '')

    try:
        db.session.commit()
        return redirect(url_for('car_bp.index'))
    except Exception as e:
        db.session.rollback()
        print("Erro ao atualizar carro:", e)
        return "Erro ao atualizar carro", 500

@car_bp.route("/delete/<int:car_id>", methods=["POST"])
def delete_car(car_id: int):
    car_to_delete = Car.query.get_or_404(car_id)
    try:
        db.session.delete(car_to_delete)
        db.session.commit()
        flash("Carro excluído com sucesso!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao excluir carro: {e}", "error")
    return redirect(url_for("car_bp.index"))
