// style css 
var style = {
    base : {
        color: '#32325d',
        fontFamily: "helvetica sans-serif",
        fontSmoothing: "antialiased",
        fontSize: "15px",
        '::placeholder': {
            color: "#aab7c4",
        }
    },
    invalid: {
        color: "#fa755a",
        iconColor: "#fa755a",
    }
  }
  
  document.addEventListener('DOMContentLoaded', async () => {
    const stripe = Stripe('pk_test_51JRFBQKoo0ZeB3KHwFkaqb6UrxYQVjW2IEpvD4MVCC5s69hbGNAs6iCaEu3RkKtQjPTRquA3yx4HN2t6IHfTY8Fq008Vkaur6D')
    const elements = stripe.elements()
    var card = elements.create("card", {style: style});
    card.mount("#card-element");
  
    card.addEventListener('change', function(event){
      var displayError=document.getElementById("card-errors")
      if (event.errors) {
          displayError.textContent = event.error.message
      }else{
          displayError.textContent = ''
      }
    })
  
    // create stripe token 
    var form = document.getElementById("payment-form")
    form.addEventListener('submit', function(event){
        event.preventDefault()
        stripe.createToken(card).then(function(result){
            if (result.error) {
                var errorElement = document.getElementById("card-errors")
                errorElement.textContent = result.error.message
            }else{
                stripeTokenHandler(result.token)
            }
        })
    })
  
    // append stripe token to the form 
    function stripeTokenHandler(token){
      var form = document.getElementById("payment-form")
      var hiddenInput = document.getElementById("input")
      hiddenInput.setAttribute('name', 'stripeToken')
      hiddenInput.setAttribute('value', token.id)
      form.appendChild(hiddenInput)
      form.submit()
    }
  
  })