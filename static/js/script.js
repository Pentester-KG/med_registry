/**
 * МедиКлиника — modal & form logic
 */

const modalOverlay = document.getElementById('modalOverlay');
const formWrap     = document.getElementById('formWrap');
const successMsg   = document.getElementById('successMsg');

/** Открыть модальное окно записи */
function openModal() {
  modalOverlay.classList.add('open');
  formWrap.style.display    = 'block';
  successMsg.style.display  = 'none';
}

/** Закрыть модальное окно */
function closeModal() {
  modalOverlay.classList.remove('open');
}

/** Закрыть при клике по фону (вне окна) */
function closeOnBackdrop(event) {
  if (event.target === modalOverlay) {
    closeModal();
  }
}

/** Обработка отправки формы */
function submitForm() {
  formWrap.style.display   = 'none';
  successMsg.style.display = 'block';
  // Автоматически закрыть через 3.2 секунды
  setTimeout(closeModal, 3200);
}

/** Закрытие по клавише Escape */
document.addEventListener('keydown', function (event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});
