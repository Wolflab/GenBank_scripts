library(rentrez)
library(mailR)

oldList <- read.csv('/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/Tanner_plastomes/all_fern_plastomes.csv')

fernQuery <- entrez_search(db="nucleotide", term="Moniliformopses[orgn] AND (plastid[titl] OR chloroplast[titl]) AND 10000:999999[slen]", retmax = 10000)
summary <- entrez_summary(db='nucleotide', id=fernQuery$ids, always_return_list = TRUE)
species <- extract_from_esummary(summary, "organism")
accessions <- extract_from_esummary(summary, "caption")
plastomeList <- cbind(species, accessions)
baseURL <- "https://www.ncbi.nlm.nih.gov/nuccore/"
i <- 1
urls <- NULL
while(i <= nrow(plastomeList)){
    if(grepl("NC_[0-9]", plastomeList[i, 2])){
        plastomeList <- plastomeList[-i,]
        next
    }
    urls <- c(urls, paste(baseURL, plastomeList[i, 2], sep = ''))
    i <- i + 1
}
plastomeList <- cbind(plastomeList, urls)
knownAccessions <- as.character(oldList$accessions)
queriedAccessions <- as.character(plastomeList[,2])
missingAccessions <- queriedAccessions[!(queriedAccessions %in% knownAccessions)] 
newURLs <- NULL
for(i in 1:length(missingAccessions)){
  newURLs <- paste(baseURL, missingAccessions, sep = '')
}

if(identical(missingAccessions, character(0))){
    print("no new plastomes")
    send.mail(from ="name@emailaddress", # note that this line and below you need to enter email address
            to = c("name@emailaddress"), 
            subject = "Fern Plastome Query", 
            body= "No new plastomes at this time", 
            smtp= list(host.name = "smtp.mail.yahoo.com", port = 465, user.name = "xxxxxx", passwd = "xxxxxx", ssl = TRUE),
            authenticate = TRUE, 
            send =TRUE)
}else{
    msg1 <- paste("Plastome query found ", length(missingAccessions), " new fern plastomes under the following accessions:\n", paste(missingAccessions, collapse= '\n'), sep = '')
    write.csv(plastomeList, file='/Users/Paul13/Dropbox/docs_wolf/Python_files/research_scripts/GenBank_scripts/check_new_cp_genomes/Tanner_plastomes/all_fern_plastomes.csv')
    msg2 <- paste("\nThe plastomes can be found at the following URLs:\n", 
                  paste(newURLs, collapse = '\n'))
    body <- paste(msg1, msg2)
    send.mail(from ="name@emajl", 
              to = c("name@emailaddress"), 
              subject = "Fern Plastome Query", 
              body= body, 
              smtp= list(host.name = "smtp.mail.yahoo.com", port = 465, user.name = "xxxxxxxxx", passwd = "xxxxxxx", ssl = TRUE),
              authenticate = TRUE, 
              send =TRUE)
}