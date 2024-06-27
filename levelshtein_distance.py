import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        vocabs = f.readlines()
        results = sorted(set([word.strip().lower() for word in vocabs]))
    return results


def levenshtein_distance(word1, word2):
    # Tạo ma trận với kích thước (len(word1) + 1) x (len(word2) + 1)
    matrix = [[0 for j in range(len(word2) + 1)]
              for i in range(len(word1) + 1)]

    # Khởi tạo hàng đầu tiên và cột đầu tiên
    for i in range(len(word1) + 1):
        matrix[i][0] = i
    for j in range(len(word2) + 1):
        matrix[0][j] = j

    # Điền ma trận
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i-1] == word2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j] + 1,    # Xóa
                                   matrix[i][j-1] + 1,    # Chèn
                                   matrix[i-1][j-1] + 1)  # Thay thế

    # Trả về giá trị ở góc dưới bên phải của ma trận
    return matrix[len(word1)][len(word2)]


def correct_word(word, list_vocab):

    list_distance = []
    dict_distance = {}

    # Lặp qua từng từ trong danh sách từ vựng
    for i in range(len(list_vocab)):
        distance = levenshtein_distance(word, list_vocab[i])
        list_distance.append(distance)
        dict_distance[list_vocab[i]] = distance

    # Tìm khoảng cách nhỏ nhất trong danh sách khoảng cách
    min_distance = min(list_distance)
    # Tìm chỉ số của khoảng cách nhỏ nhất
    index = list_distance.index(min_distance)

    sorted_dict_distance = dict(
        sorted(dict_distance.items(), key=lambda item: item[1]))
    # Trả về từ gần nhất (có khoảng cách nhỏ nhất) và từ điển khoảng cách
    return list_vocab[index], sorted_dict_distance


# vocabs = load_vocab('vocab.txt')
# print(vocabs)
# result = correct_word('anhu', vocabs)
# print(result)
def main():
    st . title(" Word Correction using Levenshtein Distance ")
    st.write("This is a simple app to correct the word using Levenshtein Distance")
    word = st.text_input("Enter the word you want to correct")
    if st.button("Correct the word"):

        vocabs = load_vocab('vocab.txt')
        result = correct_word(word, vocabs)
        st.write(f"Corect word is {result[0]}")
        col1, col2 = st.columns(2)
        with col1:
            st.write("List of vocab")
            st.write(vocabs[:10])
        with col2:
            st.write("Distance")
            dict_distance = list(result[1].items())[:10]
            new_dict_distance = {}
            for key, value in dict_distance:
                new_dict_distance[key] = value
            st.write(new_dict_distance)


if __name__ == '__main__':
    main()
