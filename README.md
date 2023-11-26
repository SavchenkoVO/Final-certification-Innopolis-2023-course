# Final-certification-Innopolis-2023-course
Итоговый проект курса "Аналитика данных и машинное обучение", Иннополис, 2023

1. Общее описание проекта:

Проект представляет из себя систему по предсказанию пластового давления на основе исторических данных по скважинам реального молодого нефтегазового месторождения в Ханты-Мансийском автономном округе, Западная Сибирь.

3. Описание функциональности:

Система должна предсказывать динамику пластового давления по всем скважинам месторождения в зависимости от времени и выводить результаты прогнозирования в веб-интерфейс.

4. Технические требования:

Модули системы написаны на языке программирования Python. В основе модели машинного обучения по предсказыванию пластового давления лежит алгоритм sequence-to-sequence (seq2seq). Веб-интерфейс написан на основе фреймворка Flask. Проект для удобства развертывания собран в контейнер при помощи технологии Docker.

5. Интерфейс пользователя:

Интерфейс пользователя представляет из себя веб-страницу «Система по предсказыванию пластового давления нефтегазового месторождения Ханты-Мансийского автономного округа, Западная Сибирь» со списком скважин, по которым модель предсказывает дальнейшую динамику. Для каждой скважины доступна карточка с индивидуальным результатом по данной скважине.

7. Требования к производительности:

Ожидаемое время отклика системы на действия пользователя веб-странице – быстрая, так как модель уже рассчитана и должна выводить уже рассчитанные показатели.

8. План тестирования:

При оценке системы будут проведены тесты сравнения прогнозных значений с реальными. Критерии успеха тестирования выражаются в минимально допустимом отклонения расчетного значения пластового давления от фактического.

10. Критерии приемки:

Успешность проекта будет оцениваться по метрикам качества предсказания модели.
