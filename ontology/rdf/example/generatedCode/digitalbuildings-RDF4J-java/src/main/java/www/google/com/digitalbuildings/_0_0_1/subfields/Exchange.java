package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Exchange 
* the transfer of heat from one fluid stream to another.
*/
@SuppressWarnings("serial")
public class Exchange extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IExchange{

	IRI newInstance;
	public Exchange(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Exchange"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IExchange> getAllExchangesObjectsCreated(){
		Set<IExchange> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Exchange")).subjects().stream()
		.map(mapper->(IExchange)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}