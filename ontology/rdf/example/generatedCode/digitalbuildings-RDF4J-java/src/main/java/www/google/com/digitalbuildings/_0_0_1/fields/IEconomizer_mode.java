package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IEconomizer;
import www.google.com.digitalbuildings._0_0_1.subfields.IMode;

public interface IEconomizer_mode extends IField{

	public IRI iri();

    public void addComposedOfEconomizer (IEconomizer parameter);

	public Set<IEconomizer> getComposedOfEconomizer();

    public void addComposedOfMode (IMode parameter);

	public Set<IMode> getComposedOfMode();

}