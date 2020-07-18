package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IExhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IDamper;

public interface IExhaust_air_damper_status extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfDamper (IDamper parameter);

	public Set<IDamper> getComposedOfDamper();

    public void addComposedOfExhaust (IExhaust parameter);

	public Set<IExhaust> getComposedOfExhaust();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}