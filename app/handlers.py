import re
from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboard as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(photo='https://a.d-cd.net/5R-DnEI6hXVpm0Y_5TMKVuVNkrE-960.jpg',
                               caption=f'Dzień dobry {message.from_user.first_name} 🙋\n'
                                        'Cieszymy się, że widzimy Cię w naszym Warsztacie, 🤤\n'
                                        'Możesz się zarejestrować, aby utrzymać kontakt,\n'
                                        'Sprawdź także nasze informacje poniżej!  👇↓👇↓👇↓👇',
                               reply_markup=kb.re_cmd)


@router.message(F.text == 'Rejestracja 📋')
async def st_mach(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer(text='Wpisz swoje imię: ')


@router.message(Reg.name)
async def st_reg0(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Wprowadź swój numer telefonu: ')


@router.message(Reg.number)
async def st_reg1(message: Message, state: FSMContext):
    await state.update_data(number=message.text.strip())
    data = await state.get_data()
    await message.answer(text=f'Imie :{data['name']}\nNumer :{data['number']}\nDziękujemy za rejestrację. \n'
                              'Bardzo cieszymy się, że jesteś z nami.  😊 💞 😊\n'
                              'Przejdź dalej 👇🏾👇🏻👇🏾👇🏻👇🏾👇🏻',
                         reply_markup=kb.re_next_reg)
    await state.clear()


@router.message(F.text == 'Warsztat 🔧')
async def war(message: Message):
    await message.answer_photo(photo='https://avatars.mds.yandex.net/i?id=be46b5aafdbdc7089388fb7a50b82978_l-5435996-'
                                     'images-thumbs&ref=rim&n=13&w=999&h=605',
                               caption='Czym dokładnie jesteś zainteresowany? 🤔',
                               reply_markup=kb.in_next_reg)


@router.callback_query(F.data == 'olej')
async def call_ol(callback: CallbackQuery):
    await callback.message.edit_caption(text='Wybierz czas ⌚\n'
                                      'Lub zostaw prośbę, a wkrótce się z Tobą skontaktujemy 🔽',
                                       reply_markup=await kb.in_next_re())


@router.callback_query(F.data == 'dia')
async def diagnostyka(callback: CallbackQuery):
    await callback.message.edit_caption(text='Hello',
                                        reply_markup=await kb.in_diagnos())


@router.callback_query(F.data == 'rem')
async def ele(callback: CallbackQuery):
    await callback.message.edit_caption(text='Jaku poczebujesz diagnostiki',
                                        reply_markup=await kb.in_dia_el())


@router.callback_query(F.data == 'mot')
async def shop(callback: CallbackQuery):
    await callback.message.edit_caption(text='Wybierz kategorije)',
                                        reply_markup=await kb.in_shop_dia())


@router.message(F.text == 'Informacje 📌')
async def cmd_info(message: Message):
    await message.answer_photo(photo='https://cdn.vectorstock.com/i/500p/35/15/sign-with-car-wrench-and-arrow-vector'
                                     '-1623515.jpg')
    await message.answer(text='  \tWarsztat jest firmą rodzinną, a jego nazwa to mieszanka teraźniejszości i'
                              ' przeszłości – kiedyś w miejscu naszego warsztatu była stajnia i padok '
                              'dla koni, dziś jesteśmy jak padok wyścigowy, gdzie maksymalnie szybko i '
                              'starannie naprawimy Twoje auto.\n'
                         
                              '  \tPadok to „dziecko” France Cars, który działa od 2005 roku. '
                              'Kontynuujemy działalność związaną z serwisem aut francuskich, ale'
                              ' poszerzyliśmy ją o samochody wszystkich marek. Nasz zakres usług jest'
                              ' szeroki: od obsługi pogwarancyjnej jak wymiana oleju, wymiana płynów'
                              ' eksploatacyjnych, serwis opon, geometria i wulkanizacja, przez układy'
                              ' zawieszenia, układy hamulcowe, układy wydechowe, układy rozrządów,'
                              ' diagnostykę i remont silnika, elektrykę i elektronikę,'
                              ' aż po regenerację tylnych belek i ozonowanie.\n'
                              '  \tOferujemy pełny zakres serwisowania aut Klientów indywidualnych oraz'
                              ' flotowych. Mamy rozsądne ceny, fach w ręku, doświadczenie i sprzęt, '
                              'a do tego miejsca do przechowywania opon i obszerny parking, na którym'
                              ' możesz postawić swoje auto długoterminowo.\n'
                         
                                        
                              '  \tWspółpracujemy z wiodącymi w regionie dystrybutorami części zamiennych, '
                              'oferując Klientom indywidualne rozwiązania, satysfakcjonujące zarówno pod '
                              'względem ceny jak i marki, a co za tym idzie – jakości. '
                              'Wiedzę regularnie uzupełniamy na szkoleniach organizowanych'
                              ' przez wiodących specjalistów z branży.\n'
                         

                              '  \tZapraszamy do kontaktu, przygotujemy ofertę'
                              ' skrojoną na miarę Twoich potrzeb.',
                         reply_markup=kb.re_info)


@router.message(F.text == 'Kontakt 📠')
async def kontakt(message:Message):
    await message.answer(text='  \n\tPostaram się pomóc rozwiązać ten problem, ponieważ starszy mechanik jest zajęty lub'
                              'warsztat jest zamknięty! 😔'
                              '  \n\tBędę Twoim asystentem i postaram się udzielić Ci odpowiedzi, jeśli zdarzy się '
                              'jakaś nieprzyjemna sytuacja...'
                              '  \n\tWybierz opcję poniżej 👇👇👇',
                         reply_markup=await kb.in_co())










