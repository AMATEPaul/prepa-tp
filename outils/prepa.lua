-- Filtre pandoc des préparations de TP.
--
-- Raccourcis Markdown -> styles Word de modele/reference.docx :
--   ::: q        question numérotée            (style Question)
--   ::: l        ligne sous la question        (style Ligne,  retrait 1)
--   ::: c        ligne de calcul               (style Calcul, retrait 2)
--   ::: capture  encadré pour une capture      (style Capture)
--   ::: schema   encadré pour un schéma        (style Schema)
--   ::: marge    note de marge                 (style Marge)
--   ::: piste    piste discrète                (style Piste)
--   [texte]{.rouge}  formule de cours / définition en rouge
--
-- Dans un bloc, chaque ligne du Markdown devient un paragraphe : pas besoin
-- de sauter une ligne entre deux lignes de calcul.

local STYLES = {
  q = "Question",
  l = "Ligne",
  c = "Calcul",
  capture = "Capture",
  schema = "Schema",
  marge = "Marge",
  piste = "Piste",
}

-- Coupe un paragraphe à chaque retour à la ligne.
local function decouper(inlines)
  local paras, courant = {}, pandoc.List()
  for _, el in ipairs(inlines) do
    if el.t == "SoftBreak" or el.t == "LineBreak" then
      paras[#paras + 1] = pandoc.Para(courant)
      courant = pandoc.List()
    else
      courant:insert(el)
    end
  end
  if #courant > 0 then paras[#paras + 1] = pandoc.Para(courant) end
  return paras
end

-- Encadrés : Word fusionne deux encadrés qui se suivent, on les sépare
-- par un paragraphe minuscule.
local ENCADRES = { capture = true, schema = true }

function Div(div)
  for classe, style in pairs(STYLES) do
    if div.classes:includes(classe) then
      local blocs = pandoc.List()
      for _, bloc in ipairs(div.content) do
        if bloc.t == "Para" or bloc.t == "Plain" then
          for _, p in ipairs(decouper(bloc.content)) do
            blocs:insert(pandoc.Div({ p }, { ["custom-style"] = style }))
          end
        else
          blocs:insert(bloc)
        end
      end
      if ENCADRES[classe] then
        blocs:insert(pandoc.Div({ pandoc.Para({ pandoc.Str("\u{200B}") }) }, { ["custom-style"] = "Separateur" }))
      end
      return blocs
    end
  end
end

-- Les équations ignorent le style du texte : on les entoure de repères
-- que vers_docx.py remplace ensuite par une couleur rouge.
function Span(span)
  if span.classes:includes("rouge") then
    local contenu = pandoc.List()
    for _, el in ipairs(span.content) do
      if el.t == "Math" then
        contenu:insert(pandoc.RawInline("openxml", "<!--rouge-debut-->"))
        contenu:insert(el)
        contenu:insert(pandoc.RawInline("openxml", "<!--rouge-fin-->"))
      else
        contenu:insert(el)
      end
    end
    return pandoc.Span(contenu, { ["custom-style"] = "Rouge" })
  end
end
