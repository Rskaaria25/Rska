# Memuat model yang telah disimpan
model = tf.keras.models.load_model('my_model.h5')

# Inisialisasi aplikasi Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        food_type = request.form['food_type']
        
        # Menggunakan model untuk mendapatkan rekomendasi makanan berdasarkan tipe
        input_vector = tfidf.transform([food_type]).toarray()
        predictions = model.predict(input_vector)
        top_k_indices = np.argsort(predictions.flatten())[::-1][:20]
        recommendations = data.loc[top_k_indices, 'Nama'].values.tolist()
        
        return render_template('recommendations.html', recommendations=recommendations)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()