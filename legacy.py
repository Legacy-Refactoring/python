def register_customer(username, email, password, full_name, phone='', country='RS', city='', address=''):
    pass


def login_customer(username, password):
    pass


def get_customer(customer_id):
    pass


def update_customer_profile(customer_id, new_email, new_phone, new_address):
    pass


def reset_password(email, new_password):
    pass


def verify_email(token):
    pass


def add_payment_method(customer_id, type, card_number, expiry_month, expiry_year, cvv, holder_name, iban=''):
    pass


def list_payment_methods(customer_id):
    pass


def delete_payment_method(pm_id):
    pass


def process_payment(customer_id, payment_method_id, amount, currency='EUR', external_order_id=None, ip=None):
    pass


def list_payments(customer_id):
    pass


def get_payment_details(payment_id):
    pass


def create_refund(payment_id, amount, reason='customer request'):
    pass


def process_refund(refund_id):
    pass


def simulate_chargeback(payment_id, amount, reason='fraud'):
    pass


def resolve_chargeback(chargeback_id, won='true'):
    pass


def create_fraud_review(payment_id, customer_id, score='85'):
    pass


def decide_fraud_review(review_id, decision, reviewer_email, reviewer_password):
    pass


def admin_list_all_customers():
    pass


def admin_export_all_data():
    pass


def search_payments(search_term):
    pass


def process_recurring_billing():
    pass


def handle_webhook(payload):
    pass


def ban_customer(customer_id):
    pass


def generate_api_key(customer_id):
    pass
